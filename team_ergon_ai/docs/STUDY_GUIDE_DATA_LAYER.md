# Universal Data Cleaning & Pipeline Playbook
> **A step-by-step algorithmic guide to taking raw, malformed extracts (PDFs, OCR, messy tables) and turning them into clean, ground-truth-ready tabular datasets.**

---

## The Master 7-Step Algorithm

```
[ Raw Messy Data / PDF Extract ]
               │
               ▼
  1. Standardize Headers & Columns       (Snake_case, strip punctuation, fix multi-line headers)
               │
               ▼
  2. Drop Noise & Ghost Rows             (Page breaks, repeated headers, '---' separator lines)
               │
               ▼
  3. Split Glued / Merged Columns        (Separate fused intervals like '120.5 - 125.0')
               │
               ▼
  4. Sanitize Numeric Fields             (European commas '12,5', strip units 'm, %', convert to float)
               │
               ▼
  5. Handle Nulls & Unmerged Cells       (Forward-fill group spans; distinguish 0.0 from NaN)
               │
               ▼
  6. Domain Logic & Physical Validation  (Interval check: to > from; recovery 0-100%; order)
               │
               ▼
  7. Final Schema Harmonization          (Explicit types, stable column order, export to CSV)
               │
               ▼
[ Ground-Truth & LLM-Ready Dataset ]
```

---

## Step 1: Standardize Headers & Column Names

### What this step does:
Raw extracts usually have messy column names containing spaces, symbols (`#`, `%`, `(m)`), or headers split across multiple rows in the original document.

### Real-World Edge Cases:
* **Multi-line headers:** Row 0 has `["Core", "Depth", "Recovery"]` and Row 1 has `["No.", "(m)", "(%)"]`. If unhandled, pandas names them `Unnamed: 0`.
* **Invisible characters & trailing spaces:** `"Depth "` is not recognized as `"Depth"`.
* **Punctuation & units in names:** Names like `Core #` or `Recovery (%)` cause issues in SQL, databases, and Python dot notation.

### Code:
```python
import re
import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes all column names to clean snake_case:
    - Strips whitespace
    - Replaces symbols (#, %, etc.) with clean text
    - Replaces spaces and dashes with underscores
    - Converts to lowercase
    """
    df = df.copy()
    cleaned_cols = []
    
    for col in df.columns:
        c = str(col).strip()
        c = c.replace("%", "pct").replace("#", "no")
        c = re.sub(r"[^\w\s]", "", c)        # Remove brackets, slashes, punctuation
        c = re.sub(r"\s+", "_", c)           # Replace spaces with single underscore
        cleaned_cols.append(c.lower())
        
    df.columns = cleaned_cols
    return df
```

---

## Step 2: Remove Noise & Ghost Rows

### What this step does:
PDF table extraction tools often dump footers, page numbers, repeated headers from page breaks, and decorative separator dashes (`----------------`) into data rows.

### Real-World Edge Cases:
* **Repeated column headers:** Every new page repeats the table header inside the data rows.
* **Decorative separator lines:** Rows consisting entirely of dashes, underscores, or equals signs (`"---"`, `"==="`).
* **Footnotes and totals:** Bottom rows saying `"Total Recovered: 15.4m"` or `"* Core jammed"`.
* **Empty / trailing rows:** Rows created by trailing whitespace or blank table rows.

### Code:
```python
def drop_noise_rows(df: pd.DataFrame, key_column: str, header_keywords: list = None) -> pd.DataFrame:
    """
    Removes junk rows like repeat headers, separator lines, and footnotes.
    `key_column`: A column that MUST have a valid value for the row to be legitimate.
    """
    df = df.copy()
    if header_keywords is None:
        header_keywords = ["total", "page", "core", "depth", "continued"]

    # 1. Drop rows where key column is completely empty
    df = df.dropna(subset=[key_column])

    # 2. Filter out separator lines (e.g., '---', '===')
    df = df[~df[key_column].astype(str).str.contains(r"^[-=_]{2,}$", regex=True)]

    # 3. Filter out repeated headers or footnote rows in key column
    pattern = "|".join([re.escape(k) for k in header_keywords])
    df = df[~df[key_column].astype(str).str.lower().str.contains(pattern, regex=True)]

    return df.reset_index(drop=True)
```

---

## Step 3: Split Glued / Merged Columns

### What this step does:
When table borders are narrow or absent, text extractors often glue adjacent columns together into a single string (e.g. `Depth From` and `Depth To` extracted together as `"120.5 - 125.0"` or `"120.5 125.0"`).

### Real-World Edge Cases:
* **Fused numerical values:** Two numbers separated only by a space or tab inside a single cell.
* **Interval notation:** Ranges written as `"120.5 - 125.0 m"` instead of two discrete columns.
* **Inconsistent separators:** Some rows use `-`, some use `to`, some use `/`.

### Code:
```python
def split_range_column(df: pd.DataFrame, source_col: str, col_from: str, col_to: str) -> pd.DataFrame:
    """
    Splits a single combined range column (e.g. '120.0 - 125.5') into two separate columns.
    """
    df = df.copy()
    pattern = r"([0-9]+(?:\.[0-9]+)?)\s*(?:-|to|/|\s)\s*([0-9]+(?:\.[0-9]+)?)"
    extracted = df[source_col].astype(str).str.extract(pattern)
    
    df[col_from] = extracted[0]
    df[col_to] = extracted[1]
    return df
```

---

## Step 4: Sanitize Numeric Fields & Strip Units

### What this step does:
Computations, sorting, and ground-truth comparisons fail if numbers are trapped as strings containing unit labels, commas, or accounting notations.

### Real-World Edge Cases:
* **European decimal commas:** In European and offshore reports, `12,50` means `12.50`.
* **Embedded unit symbols:** Text like `"15.2m"`, `"98%"`, `"2.45 g/cm3"`.
* **Accounting negatives:** Numbers formatted like `(12.5)` meaning `-12.5`.
* **Null placeholders:** Values like `"-"`, `"N/A"`, `"nil"`, `"*"`, or `"--"` cause runtime exceptions if passed directly to `float()`.

### Code:
```python
def sanitize_numeric(series: pd.Series) -> pd.Series:
    """
    Converts messy text series into clean numeric floats.
    Handles units, European commas, accounting brackets, and null symbols.
    """
    s = series.astype(str).str.strip()
    
    # Replace standard null placeholders with None (NaN)
    s = s.replace(r"^(?:-|--|n/a|na|nil|\*|\s*)$", None, regex=True)
    
    # Handle accounting negatives: '(12.5)' -> '-12.5'
    s = s.str.replace(r"\((.*?)\)", r"-\1", regex=True)
    
    # European decimals: replace comma with dot
    s = s.str.replace(",", ".", regex=False)
    
    # Extract only the numerical value (digits, optional dot, optional leading minus)
    s = s.str.extract(r"([-+]?[0-9]*\.?[0-9]+)")[0]
    
    return pd.to_numeric(s, errors="coerce")
```

---

## Step 5: Handle Nulls & Unmerged Category Cells

### What this step does:
Original documents frequently use **merged cells** for group headers (e.g. "Core 1" spans 4 rows of intervals; only row 1 has the text, rows 2-4 are blank).

### Real-World Edge Cases:
* **The Merged Cell Trap:** If you drop NaNs immediately, you accidentally discard 75% of your valid measurements because their group cell was blank.
* **False Zeros:** Replacing missing numbers with `0` is dangerous! A missing recovery value is **unknown/unrecorded**, whereas `0%` means the sample was entirely lost.

### Code:
```python
def handle_merged_and_missing(df: pd.DataFrame, group_cols: list) -> pd.DataFrame:
    """
    Forward-fills group headers (simulating unmerged cells)
    without corrupting true numeric missing values.
    """
    df = df.copy()
    
    for col in group_cols:
        if col in df.columns:
            # Replace empty strings with None so ffill catches them
            df[col] = df[col].replace("", None)
            df[col] = df[col].ffill()
            
    return df
```

---

## Step 6: Domain Logic & Physical Validation

### What this step does:
This is the automated "Domain Expert" check. It verifies whether extracted numbers make physical, scientific, or geological sense before passing them to an LLM or evaluator.

### Real-World Edge Cases:
* **Inverted depth intervals:** `depth_to` is less than `depth_from` (physically impossible in straight boreholes).
* **Percentages exceeding bounds:** Values like `198%` when the real value was `98%` (OCR prepended an extraneous digit).
* **Out-of-order sequences:** Group IDs or row sequences that jump backwards.

### Code:
```python
def validate_domain_rules(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies domain-specific physical rules and flags or corrects anomalies.
    """
    df = df.copy()
    
    # 1. Interval order check
    if "depth_from" in df.columns and "depth_to" in df.columns:
        invalid_intervals = df["depth_to"] < df["depth_from"]
        if invalid_intervals.any():
            print(f"⚠️ Warning: Found {invalid_intervals.sum()} rows where depth_to < depth_from. Swapping.")
            df.loc[invalid_intervals, ["depth_from", "depth_to"]] = (
                df.loc[invalid_intervals, ["depth_to", "depth_from"]].values
            )

    # 2. Bounded percentage check
    if "recovery_pct" in df.columns:
        out_of_bounds = (df["recovery_pct"] < 0) | (df["recovery_pct"] > 105)
        if out_of_bounds.any():
            print(f"⚠️ Warning: Found {out_of_bounds.sum()} rows with suspicious recovery %. Flagging.")
            df["is_suspicious_recovery"] = out_of_bounds

    return df
```

---

## Step 7: The Master Notebook Pipeline

This is how you structure your code so that judges and evaluators can clearly see your thought process and modular architecture:

```python
def clean_dataset_pipeline(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    End-to-End Modular Cleaning Pipeline.
    Combines every step into a verifiable, readable chain.
    """
    print(f"Initial raw shape: {raw_df.shape}")
    
    clean_df = (
        raw_df
        .pipe(clean_column_names)                                  # Step 1: Normalize header names
        .pipe(drop_noise_rows, key_column="core_no")               # Step 2: Strip page footers & junk
        .pipe(handle_merged_and_missing, group_cols=["core_no"])   # Step 3: Forward-fill merged groups
        .assign(
            # Step 4: Sanitize all numerical columns
            depth_from   = lambda d: sanitize_numeric(d["depth_from"]),
            depth_to     = lambda d: sanitize_numeric(d["depth_to"]),
            length_m     = lambda d: sanitize_numeric(d["length_m"]),
            recovery_pct = lambda d: sanitize_numeric(d["recovery_pct"]),
        )
        .pipe(validate_domain_rules)                              # Step 5: Physical validity checks
        .drop_duplicates()                                         # Step 6: Deduplicate
        .reset_index(drop=True)
    )
    
    print(f"Cleaned output shape: {clean_df.shape}")
    return clean_df
```
