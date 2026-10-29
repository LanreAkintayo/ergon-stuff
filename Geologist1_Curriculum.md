# Team Ergon: Geologist 1 — Complete Preparation Curriculum
### Role: Data & Ingestion Specialist
### Duration: 3 Weeks (21 Days) | ~1 to 1.5 hours per day
### Tool: Google Colab (free, browser-based, zero installation required)

---

> [!IMPORTANT]
> **Before anything else**: Create a free Google account (if you don't have one) and go to [colab.research.google.com](https://colab.research.google.com). Every exercise in this curriculum is done inside a Colab notebook. You do not need to install Python, terminals, or any software on your computer.

---

## The Mission in One Sentence
> By November 7, you will write a Python script that takes a messy, real oilfield PDF report and outputs a clean, tagged, structured JSON file that the AI backend can understand and search.

That is your one deliverable. Everything in this curriculum exists to get you to that point.

---

## Section 0: The Prerequisites (Before Day 1)
*Estimated time: 2–3 hours. Do these BEFORE starting Week 1.*

### 0.1 — Set Up Your Workspace
1. Go to [colab.research.google.com](https://colab.research.google.com).
2. Click **"New Notebook"**.
3. Rename it to `Team_Ergon_Geologist1.ipynb`.
4. You will see a grey box called a "cell." This is where you write code.
5. Type this in the first cell and press `Shift + Enter`:
   ```python
   print("Hello, Team Ergon!")
   ```
   If you see the words `Hello, Team Ergon!` appear below — **your environment is working.** You are ready.

### 0.2 — Understand What a "Cell" is in Colab
- A Colab notebook is made of **cells**.
- Each cell holds a block of code.
- You run a cell by pressing **`Shift + Enter`**.
- The output appears directly below the cell.
- You can add a new cell by clicking `+ Code` at the top.

### 0.3 — Understand Your Role in One Picture

```
Messy PDF (50 pages, oilfield jargon, scanned tables)
        ↓  [YOUR Python Script]
Clean chunks of text, each tagged with well name, depth, page number
        ↓  [CS 1 hands to ChromaDB]
AI can now search, find, and cite the exact answer instantly
```

You are responsible for the top section. Without you, the AI has nothing to search.

---

## Week 1: Python Foundations — The 7 Concepts You Actually Need
*Goal: Get comfortable reading and writing basic Python without fear.*

> [!NOTE]
> You do NOT need to learn everything about Python. You only need these 7 concepts. Nothing else.

---

### Day 1: Strings & Print Statements (The Very Foundation)

A **string** is just text wrapped in quotation marks. It is how Python holds words, sentences, and geological descriptions.

**Read and run this code:**
```python
# A string is just text in quotes
well_name = "OML-42 Well-01"
formation = "Agbada Formation"
description = "The reservoir sand was encountered at 9,200 ft TVDSS."

# Print combines and shows them
print("Well:", well_name)
print("Formation:", formation)
print("Description:", description)
```

**Practice Task (Day 1):**
Create 4 variables describing a fake well:
- `well_name`
- `field_name`
- `reservoir_type`
- `drilling_year`

Print all 4 on separate lines.

---

### Day 2: Numbers, Math, and Basic Conditions

**Numbers in Python:**
```python
# Integer (whole number)
depth_ft = 9200

# Float (decimal number)
porosity = 0.24   # 24%
net_pay = 47.5    # metres

# Basic math
depth_m = depth_ft * 0.3048  # Convert feet to metres
print("Depth in metres:", depth_m)

# Petrophysical formula: Vshale
GR = 65.0         # Gamma Ray reading
GR_min = 15.0     # Clean sand baseline
GR_max = 120.0    # Pure shale baseline

Vshale = (GR - GR_min) / (GR_max - GR_min)
print("Volume of Shale:", round(Vshale, 3))
```

**Basic Conditions (if / else):**
```python
# Check if a porosity value is valid
porosity = -999.25   # This is a standard "missing data" code in oilfield logs

if porosity == -999.25:
    print("Missing data — skip this reading")
else:
    print("Valid porosity:", porosity)
```

**Practice Task (Day 2):**
Write an `if/else` that checks whether a Gamma Ray reading is "Sand" or "Shale":
- GR < 75 → print "Clean Sand"
- GR >= 75 → print "Shale"

---

### Day 3: Lists — Holding Multiple Things

A **list** is a collection of items stored in one variable. Think of it as your Excel column in Python.

```python
# A list of well names
wells = ["OML-42 Well-01", "OML-42 Well-02", "OML-118 Bonga-01"]

# Access items by position (starts at 0)
print(wells[0])   # OML-42 Well-01
print(wells[2])   # OML-118 Bonga-01

# Add a new well
wells.append("OML-58 Egina-03")
print(wells)

# How many wells do we have?
print("Total wells:", len(wells))

# Loop through every well
for well in wells:
    print("Processing:", well)
```

**Practice Task (Day 3):**
Create a list of 5 formation names from a Niger Delta stratigraphy column (e.g. Benin, Agbada, Akata). 
Loop through them and print: `"Formation: [name] — checking for reservoir quality..."`.

---

### Day 4: Dictionaries — The Most Important Concept in This Curriculum

A **dictionary** is a collection of key-value pairs. This is how your chunk metadata will be structured. **Understand this concept very deeply.**

```python
# A dictionary describing one chunk of well report text
chunk = {
    "text": "The Agbada Formation sandstone at 9,200 ft shows good reservoir quality with 24% porosity and 500 mD permeability.",
    "well_name": "OML-42 Well-01",
    "formation": "Agbada",
    "depth_top_ft": 9200,
    "depth_bottom_ft": 9450,
    "page_number": 14,
    "section": "Reservoir Description"
}

# Access a specific value
print(chunk["well_name"])         # OML-42 Well-01
print(chunk["depth_top_ft"])      # 9200

# Update a value
chunk["page_number"] = 15
print("Updated page:", chunk["page_number"])

# Check all keys
print(chunk.keys())
```

**A list of dictionaries (your final output format):**
```python
# Multiple chunks — this is what your final script will produce
all_chunks = [
    {
        "text": "First passage about Well-01 stratigraphy...",
        "well_name": "Well-01",
        "page_number": 1
    },
    {
        "text": "Second passage about reservoir pressure in Well-02...",
        "well_name": "Well-02",
        "page_number": 5
    }
]

# Loop through all chunks
for chunk in all_chunks:
    print(f"Well: {chunk['well_name']} | Page: {chunk['page_number']}")
    print(f"Text: {chunk['text'][:60]}...")   # Show first 60 characters only
    print("---")
```

**Practice Task (Day 4):**
Create a list of 3 chunk dictionaries manually, each with:
- `text`, `well_name`, `depth_top_ft`, `depth_bottom_ft`, `page_number`

Loop through them and print a summary line for each.

---

### Day 5: Functions — Packaging Your Work Neatly

A **function** is a block of code you write once and reuse many times. You will write a `clean_text()` function and a `tag_chunk()` function in your final script.

```python
# Define a function
def clean_text(raw_text):
    """Removes extra whitespace and newlines from extracted PDF text."""
    cleaned = raw_text.strip()       # Remove leading/trailing whitespace
    cleaned = " ".join(cleaned.split())   # Collapse multiple spaces into one
    return cleaned

# Test the function
messy = "   The  reservoir   sand  was  encountered \n at 9,200 ft.   "
result = clean_text(messy)
print(result)
# Output: "The reservoir sand was encountered at 9,200 ft."
```

```python
# A function that tags a chunk with metadata
def tag_chunk(text, well_name, page_number, section="General"):
    """Wraps a text chunk with its geological metadata."""
    return {
        "text": clean_text(text),
        "well_name": well_name,
        "page_number": page_number,
        "section": section
    }

# Test it
chunk = tag_chunk(
    text="   Porosity averages 22% across the net reservoir interval.  ",
    well_name="OML-42 Well-01",
    page_number=17,
    section="Petrophysical Analysis"
)
print(chunk)
```

**Practice Task (Day 5):**
Write a function `is_valid_depth(depth_value)` that:
- Returns `False` if the depth is `-999.25` (missing data code)
- Returns `False` if the depth is negative
- Returns `True` for any other value
Test it with 4 different depth values.

---

### Day 6: Reading Files — Text and CSV Files

Before you can read PDFs, you must understand how Python reads any file.

**Reading a plain text file:**
```python
# Write a small text file first (simulating extracted PDF text)
sample_text = """
Well Completion Report: OML-42 Well-01
Field: Assa North
Formation: Agbada
Depth: 9,200 ft to 9,450 ft
Porosity: 24%
Permeability: 500 mD
Net Pay: 47 ft
Fluid Type: Light Oil (38 API)
"""

# Save it to a file
with open("sample_well_report.txt", "w") as f:
    f.write(sample_text)

# Read it back
with open("sample_well_report.txt", "r") as f:
    content = f.read()

print(content)
```

**Reading a CSV file with pandas:**
```python
import pandas as pd

# Create a sample well log CSV first
import io
csv_data = """DEPT,GR,RHOB,NPHI,RT,LITHOLOGY
8000,95,2.55,0.32,5.2,SHALE
8050,40,2.35,0.22,85.0,SANDSTONE
8100,45,2.38,0.24,78.0,SANDSTONE
8150,110,2.65,0.35,4.1,SHALE
8200,-999.25,2.55,0.30,6.0,SHALE
"""

df = pd.read_csv(io.StringIO(csv_data))
print(df)
print("\nColumn names:", df.columns.tolist())
print("\nShape:", df.shape)   # (rows, columns)
```

**Practice Task (Day 6):**
Load the CSV above and:
1. Replace all `-999.25` values with `None` using `df.replace(-999.25, None)`.
2. Filter and print only the rows where `LITHOLOGY == "SANDSTONE"`.
3. Calculate the average `GR` for sandstone rows.

---

### Day 7: Week 1 Mini-Project (Milestone Checkpoint)

**Build this in one Colab notebook:**

You are given a raw string (simulate extracted PDF text from a well completion report). Write a script that:
1. Cleans the text (remove extra spaces, weird newlines).
2. Checks if it contains the word "Agbada" (use Python's `in` keyword: `if "Agbada" in text:`).
3. Creates a tagged chunk dictionary with: `text`, `well_name`, `page_number`, `contains_reservoir_name`.
4. Appends it to a list called `all_chunks`.
5. Prints a summary: `"Total chunks collected: X"`.

If you complete this without looking at the answer—**you are 100% ready for Week 2.**

---

## Week 2: PDF Extraction & Text Cleaning
*Goal: Read real PDF files and extract clean, structured text.*

---

### Day 8: Install and Understand `pdfplumber`

`pdfplumber` is the best Python library for extracting text from oilfield PDF reports. It handles columns and tables far better than most other libraries.

**Install it (run this in a Colab cell first):**
```python
!pip install pdfplumber
```

**Find a sample PDF to practice on:**
Download any of these free public sources:
- **SPE Papers**: [onepetro.org](https://www.onepetro.org) (search "Niger Delta" for free papers)
- **NUPRC/DPR Reports**: Search Google for `"Nigeria field development plan filetype:pdf"`
- **Volve Open Dataset**: [equinor.com/energy/volve-data-sharing](https://www.equinor.com/energy/volve-data-sharing) (free Norwegian field, same concepts)

Upload the PDF into Colab by clicking the **folder icon** on the left sidebar → **Upload** button.

**Your first PDF reader:**
```python
import pdfplumber

pdf_path = "your_well_report.pdf"   # Replace with your uploaded filename

with pdfplumber.open(pdf_path) as pdf:
    total_pages = len(pdf.pages)
    print(f"Total pages in PDF: {total_pages}")
    
    # Read the first 3 pages
    for i in range(min(3, total_pages)):
        page = pdf.pages[i]
        text = page.extract_text()
        
        print(f"\n--- PAGE {i+1} ---")
        print(text[:500])   # Print first 500 characters only
```

**Practice Task (Day 8):**
Read your sample PDF and print the first 200 characters of every page. Note which pages contain reservoir data, which contain tables, and which are cover/contents pages.

---

### Day 9: Stripping Headers, Footers, and Noise

Every oilfield PDF has repeated noise that confuses the AI: company logos turned into garbled text, repeated page headers, and footer stamps.

```python
def clean_page_text(raw_text, page_number):
    """
    Cleans extracted text from a single PDF page.
    Removes empty lines, repeated headers, and junk characters.
    """
    if raw_text is None:
        return ""
    
    lines = raw_text.split("\n")
    cleaned_lines = []
    
    # Common oilfield PDF junk patterns to filter out
    junk_patterns = [
        "confidential",
        "proprietary",
        "page " + str(page_number),
        "shell petroleum",       # Add your company name
        "all rights reserved",
    ]
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if len(line) == 0:
            continue
        
        # Skip lines that are just numbers (page numbers)
        if line.isdigit():
            continue
        
        # Skip lines containing junk patterns (case-insensitive)
        is_junk = any(pattern in line.lower() for pattern in junk_patterns)
        if is_junk:
            continue
        
        cleaned_lines.append(line)
    
    return " ".join(cleaned_lines)


# Test it on your PDF
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages[:5]):
        raw = page.extract_text()
        cleaned = clean_page_text(raw, i + 1)
        print(f"\n--- Page {i+1} CLEANED ---")
        print(cleaned[:400])
```

**Practice Task (Day 9):**
Customize the `junk_patterns` list for your specific PDF. Read 5 pages and verify the noise is gone.

---

### Day 10: Extracting Tables from PDFs

Stratigraphy tables, pressure-depth tables, and core analysis tables are the most valuable data in a well report—and the hardest to extract. `pdfplumber` handles them well.

```python
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        
        if tables:
            print(f"\n--- Tables found on Page {i+1} ---")
            for table_num, table in enumerate(tables):
                print(f"  Table {table_num+1}: {len(table)} rows x {len(table[0])} columns")
                
                # Print first 3 rows of each table
                for row in table[:3]:
                    print("  ", row)
```

**Converting a table to a readable string (to feed to the AI):**
```python
def table_to_text(table, table_title="Data Table"):
    """Converts an extracted table list into a readable string for AI ingestion."""
    if not table or len(table) < 2:
        return ""
    
    headers = table[0]   # First row is usually column headers
    text_rows = [f"[{table_title}]"]
    
    for row in table[1:]:   # Skip header row
        if row and any(cell for cell in row):   # Skip empty rows
            row_text = " | ".join([str(cell) if cell else "N/A" for cell in row])
            text_rows.append(row_text)
    
    return "\n".join(text_rows)

# Test it
with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[5]   # Pick a page you know has a table
    tables = page.extract_tables()
    if tables:
        result = table_to_text(tables[0], "Stratigraphy Column")
        print(result)
```

**Practice Task (Day 10):**
Find a page in your PDF that has a table (lithology, stratigraphy, or core analysis). Extract the table and convert it to readable text using `table_to_text()`.

---

### Day 11: Full Page Extractor — Combining Text & Tables

Now we combine everything from Days 8–10 into a single function that extracts a full page:

```python
def extract_page_content(page, page_number):
    """
    Extracts all content (text + tables) from a single PDF page.
    Returns a clean, combined string ready for chunking.
    """
    content_parts = []
    
    # 1. Extract and clean the main text
    raw_text = page.extract_text()
    if raw_text:
        clean = clean_page_text(raw_text, page_number)
        if clean:
            content_parts.append(clean)
    
    # 2. Extract and convert any tables
    tables = page.extract_tables()
    for table in tables:
        table_text = table_to_text(table)
        if table_text:
            content_parts.append(table_text)
    
    # Combine text and table content
    return "\n\n".join(content_parts)


# Extract the entire PDF
def extract_full_pdf(pdf_path):
    """Extracts all pages from a PDF into a list of page content strings."""
    pages_content = []
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Extracting {len(pdf.pages)} pages...")
        
        for i, page in enumerate(pdf.pages):
            content = extract_page_content(page, i + 1)
            
            if content.strip():   # Only add pages that have content
                pages_content.append({
                    "page_number": i + 1,
                    "content": content
                })
            
            if (i + 1) % 10 == 0:
                print(f"  Processed {i+1} pages...")
    
    print(f"Extraction complete. {len(pages_content)} pages with content.")
    return pages_content


# Run it on your PDF
pages = extract_full_pdf(pdf_path)
print(f"\nSample from page 3:")
print(pages[2]["content"][:500])
```

**Practice Task (Day 11):**
Run `extract_full_pdf()` on your sample PDF. Print a summary of each page (page number + first 100 characters). Verify the tables are being captured.

---

### Day 12: Text Chunking (The Core Skill)

A "chunk" is a fixed-size piece of text that the vector database will store and search. Too small (< 100 words) and chunks lose context. Too large (> 1,000 words) and the AI gets confused.

**Install LangChain's text splitter:**
```python
!pip install langchain-text-splitters
```

**Your chunking function:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text, chunk_size=500, chunk_overlap=100):
    """
    Splits a long text into overlapping chunks.
    chunk_overlap means the last 100 chars of chunk 1 are repeated at the
    start of chunk 2 — this prevents losing context at boundaries.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", " "]
    )
    
    chunks = splitter.split_text(text)
    return chunks


# Test it
long_text = " ".join([pages[i]["content"] for i in range(3)])   # Combine 3 pages

chunks = chunk_text(long_text)
print(f"Total chunks created: {len(chunks)}")
print(f"\nChunk 1 ({len(chunks[0])} chars):")
print(chunks[0])
print(f"\nChunk 2 ({len(chunks[1])} chars):")
print(chunks[1])
print("\nNotice how chunk 2 starts with the end of chunk 1 (overlap).")
```

**Practice Task (Day 12):**
Experiment with `chunk_size = 300`, `400`, and `600`. Print the first 3 chunks for each setting. Decide which size preserves geological sentences best without cutting formations in half.

---

### Day 13: Domain-Aware Chunking — Where Your Geology Knowledge Matters

Generic text splitters don't understand geology. You need to add your domain expertise as custom splitting rules.

```python
# Domain-specific separator list — petroleum report section headers
# The splitter will try to break at these boundaries FIRST before splitting mid-sentence
PETROLEUM_SEPARATORS = [
    "\n\nWELL SUMMARY",
    "\n\nRESERVOIR DESCRIPTION",
    "\n\nSTRATIGRAPHY",
    "\n\nPETROPHYSICAL ANALYSIS",
    "\n\nDRILLING PARAMETERS",
    "\n\nPRESSURE DATA",
    "\n\nCOMPLETION SUMMARY",
    "\n\nPRODUCTION HISTORY",
    "\n\nCORE ANALYSIS",
    "\n\nWELL RECOMMENDATIONS",
    "\n\n",   # Fallback: paragraph breaks
    "\n",     # Fallback: line breaks
    ". ",     # Fallback: sentence ends
    " "       # Last resort: word boundaries
]

def domain_chunk_text(text, chunk_size=500, chunk_overlap=100):
    """Splits petroleum report text at natural geological section boundaries."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=PETROLEUM_SEPARATORS
    )
    return splitter.split_text(text)
```

> [!TIP]
> Add any specific section headers you find in your actual oilfield PDF to the `PETROLEUM_SEPARATORS` list. The more specific you make this, the better your chunks will be.

**Practice Task (Day 13):**
Compare `chunk_text()` (generic) vs `domain_chunk_text()` (geological) on the same PDF page. Print side-by-side and see how the section boundaries differ.

---

### Day 14: Week 2 Milestone — Full Extractor Script

**Build this complete pipeline:**

```python
import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = "your_well_report.pdf"
well_name = "OML-42 Well-01"         # You define this manually per report

# Step 1: Extract all pages
pages = extract_full_pdf(pdf_path)

# Step 2: Chunk each page with domain-aware splitting
all_raw_chunks = []

for page_data in pages:
    page_number = page_data["page_number"]
    content = page_data["content"]
    
    chunks = domain_chunk_text(content, chunk_size=500, chunk_overlap=100)
    
    for chunk in chunks:
        if len(chunk.strip()) > 50:   # Ignore tiny, meaningless chunks
            all_raw_chunks.append({
                "text": chunk.strip(),
                "page_number": page_number,
                "well_name": well_name
            })

print(f"Total raw chunks: {len(all_raw_chunks)}")

# Step 3: Preview
for chunk in all_raw_chunks[:3]:
    print(f"\nPage {chunk['page_number']} | {len(chunk['text'])} chars")
    print(chunk["text"][:200])
    print("---")
```

If this runs without errors and produces a list of clean, readable chunks — **you have completed Week 2.**

---

## Week 3: Metadata Tagging, JSON Export & Team Hand-off
*Goal: Add rich metadata to every chunk and export the final JSON file.*

---

### Day 15: Keyword Detection — Auto-Tagging Chunks

Instead of manually reading every chunk, write a function that automatically detects what geological topic a chunk discusses.

```python
# Keyword dictionaries for auto-tagging geological content
FORMATION_KEYWORDS = [
    "agbada", "benin", "akata", "qua iboe", "coastal plain sands",
    "imo formation", "paleocene", "eocene", "oligocene", "miocene"
]

RESERVOIR_KEYWORDS = [
    "porosity", "permeability", "net pay", "reservoir", "sand",
    "sandstone", "hydrocarbon", "oil", "gas", "condensate"
]

DRILLING_KEYWORDS = [
    "mud weight", "drilling", "casing", "bit size", "deviation",
    "inclination", "azimuth", "kick", "blowout", "spud date"
]

PRESSURE_KEYWORDS = [
    "pressure", "psi", "formation pressure", "hydrostatic",
    "overpressure", "abnormal pressure", "RFT", "MDT", "DST"
]

def detect_section(text):
    """Auto-detects what geological section a chunk belongs to."""
    text_lower = text.lower()
    
    if any(kw in text_lower for kw in RESERVOIR_KEYWORDS):
        return "Reservoir Description"
    elif any(kw in text_lower for kw in FORMATION_KEYWORDS):
        return "Stratigraphy"
    elif any(kw in text_lower for kw in PRESSURE_KEYWORDS):
        return "Pressure Data"
    elif any(kw in text_lower for kw in DRILLING_KEYWORDS):
        return "Drilling Parameters"
    else:
        return "General"


# Test it on your chunks
for chunk in all_raw_chunks[:10]:
    section = detect_section(chunk["text"])
    print(f"Page {chunk['page_number']} → Detected section: {section}")
    print(chunk["text"][:100])
    print("---")
```

**Practice Task (Day 15):**
Add more keywords from your actual PDF vocabulary to the dictionaries above. Run detection on your chunks and verify the labels make geological sense.

---

### Day 16: Depth Extraction — Pulling Numbers from Text

The most valuable metadata you can add is the depth range discussed in a chunk. Write a function that extracts depth numbers from text automatically.

```python
import re

def extract_depth_mention(text):
    """
    Extracts the first depth value mentioned in text.
    Handles formats like: '9,200 ft', '9200ft', '2804 m', '9200 TVDSS'
    """
    # Pattern: optional comma-separated number followed by ft, m, TVDSS, or MD
    pattern = r'(\d{1,2},?\d{3})\s*(ft|m\b|TVDSS|TVDMD|MD|TVD)'
    
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    if matches:
        # Return the first match, cleaned up
        depth_str = matches[0][0].replace(",", "")
        unit = matches[0][1].upper()
        return int(depth_str), unit
    
    return None, None


# Test it
test_texts = [
    "The Agbada Formation sandstone was penetrated at 9,200 ft TVDSS.",
    "Core recovered from 2,804 m to 2,850 m shows excellent porosity.",
    "No depth mentioned in this introductory paragraph.",
    "Drilling continued to 11,500ft before casing was set."
]

for text in test_texts:
    depth, unit = extract_depth_mention(text)
    print(f"Depth found: {depth} {unit}")
```

**Practice Task (Day 16):**
Run `extract_depth_mention()` on your first 20 chunks. For chunks where depth is detected, add it to the chunk metadata dictionary.

---

### Day 17: Building the Full Metadata Tagger

Now combine everything into the final metadata tagging function:

```python
def tag_chunk_full(text, well_name, page_number, report_year=None, field_name=None):
    """
    Takes a raw text chunk and adds comprehensive geological metadata.
    This is your final, production-ready tagging function.
    """
    depth, depth_unit = extract_depth_mention(text)
    section = detect_section(text)
    
    return {
        "text": text,
        "metadata": {
            "well_name": well_name,
            "field_name": field_name or "Unknown",
            "page_number": page_number,
            "section": section,
            "depth_mentioned": depth,
            "depth_unit": depth_unit,
            "report_year": report_year,
            "char_length": len(text)
        }
    }


# Apply to all chunks
all_tagged_chunks = []

for chunk in all_raw_chunks:
    tagged = tag_chunk_full(
        text=chunk["text"],
        well_name=well_name,
        page_number=chunk["page_number"],
        report_year=2023,
        field_name="Assa North"
    )
    all_tagged_chunks.append(tagged)

print(f"Total tagged chunks: {len(all_tagged_chunks)}")
print("\nSample tagged chunk:")
import json
print(json.dumps(all_tagged_chunks[0], indent=2))
```

---

### Day 18: Exporting the Final JSON File

```python
import json

output_filename = "well_report_chunks.json"

with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(all_tagged_chunks, f, indent=2, ensure_ascii=False)

print(f"✅ Exported {len(all_tagged_chunks)} tagged chunks to {output_filename}")

# Verify by reading it back
with open(output_filename, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"✅ Verification: {len(loaded)} chunks loaded successfully.")
print(f"\nFirst chunk preview:")
print(f"  Well: {loaded[0]['metadata']['well_name']}")
print(f"  Page: {loaded[0]['metadata']['page_number']}")
print(f"  Section: {loaded[0]['metadata']['section']}")
print(f"  Text: {loaded[0]['text'][:150]}...")
```

**Download the JSON from Colab:**
- Click the **folder icon** on the left sidebar.
- Right-click `well_report_chunks.json`.
- Click **Download**.
- Send this file to your CS 1.

---

### Day 19: Process Multiple PDFs (The Real Hackathon Scenario)

On November 7, NAPE may give you 5 to 20 PDFs — not just one. Your script must handle multiple files automatically.

```python
import os

def process_multiple_pdfs(pdf_folder_path, output_filename="all_chunks.json"):
    """
    Processes all PDF files in a folder and merges their chunks.
    """
    all_chunks = []
    pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]
    
    print(f"Found {len(pdf_files)} PDF files to process.")
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder_path, pdf_file)
        
        # Derive well name from filename (e.g. "OML42-Well01-Completion.pdf" → "OML42-Well01")
        well_name = pdf_file.replace(".pdf", "").split("-")[0]
        
        print(f"\nProcessing: {pdf_file}")
        
        # Extract pages
        pages = extract_full_pdf(pdf_path)
        
        # Chunk pages
        for page_data in pages:
            chunks = domain_chunk_text(page_data["content"])
            for chunk in chunks:
                if len(chunk.strip()) > 50:
                    tagged = tag_chunk_full(
                        text=chunk.strip(),
                        well_name=well_name,
                        page_number=page_data["page_number"]
                    )
                    all_chunks.append(tagged)
    
    # Export combined JSON
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Done! {len(all_chunks)} total chunks from {len(pdf_files)} PDFs.")
    print(f"Saved to: {output_filename}")
    return all_chunks
```

---

### Day 20: Quality Check & Validation

Before handing the JSON to the CS 1, run this quality check:

```python
def validate_chunks(chunks):
    """
    Quality checks all chunks and reports issues.
    Run this before handing off to the CS teammate.
    """
    issues = []
    
    for i, chunk in enumerate(chunks):
        text = chunk.get("text", "")
        metadata = chunk.get("metadata", {})
        
        # Check 1: Empty or tiny text
        if len(text.strip()) < 30:
            issues.append(f"Chunk {i}: Text too short ({len(text)} chars)")
        
        # Check 2: Missing well name
        if not metadata.get("well_name") or metadata["well_name"] == "Unknown":
            issues.append(f"Chunk {i} (Page {metadata.get('page_number')}): Missing well name")
        
        # Check 3: Text is gibberish (too many non-alphabetic characters)
        alpha_ratio = sum(c.isalpha() for c in text) / max(len(text), 1)
        if alpha_ratio < 0.4:
            issues.append(f"Chunk {i}: Possible garbled text (only {alpha_ratio:.0%} alphabetic)")
    
    if issues:
        print(f"⚠️ Found {len(issues)} issues:")
        for issue in issues[:10]:   # Show first 10 issues
            print(f"  - {issue}")
    else:
        print(f"✅ All {len(chunks)} chunks passed quality checks!")
    
    # Summary statistics
    print(f"\nSummary:")
    print(f"  Total chunks: {len(chunks)}")
    
    sections = [c["metadata"]["section"] for c in chunks]
    from collections import Counter
    for section, count in Counter(sections).most_common():
        print(f"  {section}: {count} chunks")

# Run validation
validate_chunks(all_tagged_chunks)
```

---

### Day 21: Offline Practice Drill (The Hackathon Simulation)

This is your most important day before November 7.

**The drill:**
1. Download a new PDF you have never seen before (find one from SPE or a public NUPRC report).
2. Set a timer for **45 minutes**.
3. Run your entire pipeline from scratch: `extract_full_pdf()` → `domain_chunk_text()` → `tag_chunk_full()` → `validate_chunks()` → `export JSON`.
4. Verify the output makes sense.
5. "Hand off" the JSON file to your CS 1.

**If you can do this in 45 minutes without looking at notes — you are ready for November 7.**

---

## Section 4: The 3 Oilfield "Messed-Up Data" Curveballs
*Goal: Ensure Geologist 1 never gets stuck when NAPE gives non-standard or messy files.*

In real Nigerian oilfield data archives, files rarely come perfectly typed and digital. Here are the 3 real-world curveballs you will encounter, and the exact 3-line solutions for each:

---

### Curveball 1: The "Scanned Paper" PDF (Image Only, No Digital Text)
* **What happens**: You open a 1992 NNPC/Shell well completion report. It looks like a PDF, but when you run `page.extract_text()`, it returns `""` (empty string) because it is a **photograph/scan** of physical paper.
* **The Solution**: **OCR (Optical Character Recognition)** using Tesseract.

```python
# Step 1: Install OCR tools in Colab (run once)
!apt-get install -y tesseract-ocr
!pip install pytesseract pillow

import pytesseract
import pdfplumber

def extract_page_with_ocr_fallback(page, page_number):
    """
    Extracts text normally. If the page is a scanned image (text is empty),
    it automatically falls back to OCR to read the text from the image!
    """
    # Try normal digital extraction first (fast)
    text = page.extract_text()
    
    # If empty or less than 20 characters, it's a scanned photocopy!
    if not text or len(text.strip()) < 20:
        print(f"  [OCR Activated] Page {page_number} is a scan. Reading image...")
        # Convert the PDF page to an image
        image = page.to_image(resolution=300).original
        # Read words from the image
        text = pytesseract.image_to_string(image)
    
    return clean_page_text(text, page_number)
```
> [!NOTE]
> This connects directly to **DeployEdu Stage 1: "Vision & OCR"**. If NAPE tests you with old scanned legacy docs to "Unlock Dormant Value," this function handles it automatically!

---

### Curveball 2: Well Log `.LAS` Files (Log ASCII Standard)
* **What happens**: NAPE hands you a folder containing files ending in `.las` (e.g. `Well_03_wireline.las`). These contain sensor curves (Gamma Ray, Resistivity, Sonic, Density vs Depth).
* **The Solution**: The `lasio` library turns any `.las` file into a pandas table in 3 lines.

```python
# Step 1: Install lasio (run once in Colab)
!pip install lasio

import lasio

def read_well_las(las_filepath):
    """
    Reads an oilfield .LAS file and converts it into clean text & table data.
    """
    # 1. Read the LAS file
    las = lasio.read(las_filepath)
    
    # 2. Extract well header metadata
    well_info = {
        "well_name": las.well.WELL.value if "WELL" in las.well else "Unknown",
        "field": las.well.FLD.value if "FLD" in las.well else "Unknown",
        "start_depth": las.well.STRT.value if "STRT" in las.well else None,
        "stop_depth": las.well.STOP.value if "STOP" in las.well else None,
        "step": las.well.STEP.value if "STEP" in las.well else None,
        "curves_available": [c.mnemonic for c in las.curves]
    }
    
    # 3. Convert curve readings into a pandas DataFrame
    df = las.df().reset_index()
    
    # Replace standard oilfield null values (-999.25) with NaN
    df = df.replace(-999.25, None)
    
    print(f"Loaded LAS for {well_info['well_name']}: {len(df)} depth samples.")
    print(f"Curves recorded: {well_info['curves_available']}")
    return well_info, df
```
Now, if you want to turn a LAS curve into a searchable chunk:
```python
def summarize_las_interval(df, well_name, top_depth, bottom_depth):
    """Creates a text chunk summarizing log curves across a reservoir interval."""
    interval_df = df[(df['DEPT'] >= top_depth) & (df['DEPT'] <= bottom_depth)]
    
    avg_gr = interval_df['GR'].mean() if 'GR' in interval_df else 'N/A'
    avg_rhob = interval_df['RHOB'].mean() if 'RHOB' in interval_df else 'N/A'
    avg_nphi = interval_df['NPHI'].mean() if 'NPHI' in interval_df else 'N/A'
    
    summary_text = (
        f"Well {well_name} interval {top_depth} ft to {bottom_depth} ft: "
        f"Average Gamma Ray is {avg_gr:.1f} API, "
        f"Average Density (RHOB) is {avg_rhob:.2f} g/cc, "
        f"Average Neutron Porosity (NPHI) is {avg_nphi:.2f} dec."
    )
    return tag_chunk_full(summary_text, well_name, page_number=1, field_name="Well Log")
```

---

### Curveball 3: Messy Multi-Tab Excel Spreadsheets
* **What happens**: You receive `field_production_history.xlsx` with merged header rows, company logos at the top, and 8 different sheets.
* **The Solution**: Master 2 `pandas` parameters: `skiprows` and `sheet_name=None`.

```python
# Step 1: Install openpyxl (for modern Excel files)
!pip install openpyxl

import pandas as pd

def read_all_excel_sheets(filepath, skip_banner_rows=0):
    """
    Reads EVERY sheet in a messy Excel workbook into separate clean DataFrames.
    """
    # sheet_name=None loads all sheets into a Python dictionary: {sheet_name: dataframe}
    all_sheets = pd.read_excel(filepath, sheet_name=None, skiprows=skip_banner_rows)
    
    cleaned_sheets = {}
    for sheet_name, df in all_sheets.items():
        # Drop rows and columns that are 100% empty
        df_clean = df.dropna(how="all").dropna(axis=1, how="all")
        print(f"Sheet '{sheet_name}': {df_clean.shape[0]} rows x {df_clean.shape[1]} cols")
        cleaned_sheets[sheet_name] = df_clean
        
    return cleaned_sheets

# If headers are on row 5 because of merged title logos:
# data = read_all_excel_sheets("messy_data.xlsx", skip_banner_rows=4)
```

---

## Final Deliverable Summary

By November 7, Geologist 1 owns the **Universal Ingestion Engine**:

```
                       [ANY RAW INPUT]
         ┌───────────────┬──────────────┬──────────────┐
         ▼               ▼              ▼              ▼
    Digital PDF      Scanned PDF      .LAS File    Excel / CSV
    (pdfplumber)     (OCR Fallback)    (lasio)       (pandas)
         │               │              │              │
         └───────────────┼──────────────┴──────────────┘
                         ▼
             STEP 1: Extract & Clean Text / Tables
                         ▼
             STEP 2: Domain-Aware Chunking (500 chars)
                         ▼
             STEP 3: Metadata Tagging (Well, Depth, Section)
                         ▼
             STEP 4: Quality Validation (validate_chunks)
                         ▼
             OUTPUT: well_report_chunks.json
             (Handed to CS 1 for Vector Database & AI search)
```

---

## Quick Reference Card (Print This!)

| Concept | One-Line Summary | When to Use |
| :--- | :--- | :--- |
| `print()` | Show output on screen | Testing any variable |
| `if / else` | Make decisions in code | Checking nulls or rock types |
| `list` | Ordered collection of items | Storing well names, chunk collections |
| `dict` | Key-value pairs | Your exact chunk metadata structure |
| `def function():` | Reusable block of code | Packaging clean & tag routines |
| `pdfplumber` | Extract digital text and tables | Clean digital PDFs |
| `pytesseract` | OCR image-to-text fallback | Scanned paper / photocopy PDFs |
| `lasio` | Parse `.las` well log curves | Sensor log files |
| `pd.read_excel()` | Load messy multi-tab spreadsheets | Production & test tabular data |
| `RecursiveCharacterTextSplitter` | Split text into chunks | Creating 500-word search pieces |
| `detect_section()` | Auto-detect geological topic | Tagging formation/reservoir/drilling |
| `extract_depth_mention()` | Regex depth extraction | Pulling ft/m/TVDSS numbers |
| `json.dump()` | Save chunks to JSON | Exporting final hand-off file |

---

## Python Libraries to Know (Nothing More)

| Library | Purpose | How to Install |
| :--- | :--- | :--- |
| `pdfplumber` | Extract text + tables from digital PDFs | `!pip install pdfplumber` |
| `pytesseract` | OCR fallback for scanned photocopy PDFs | `!apt-get install tesseract-ocr && pip install pytesseract` |
| `lasio` | Read oilfield `.las` well log curve files | `!pip install lasio` |
| `openpyxl` | Read modern Excel (`.xlsx`) files | `!pip install openpyxl` |
| `pandas` | Read and clean CSV/Excel files | Pre-installed in Colab |
| `langchain-text-splitters` | Smart text chunking | `!pip install langchain-text-splitters` |
| `json` | Export/import JSON files | Pre-installed in Python |
| `re` | Extract patterns (depth numbers) from text | Pre-installed in Python |
| `os` | Work with files and folders | Pre-installed in Python |

---

> [!CAUTION]
> **Do NOT try to learn anything beyond this list.** Django, Flask, NumPy, TensorFlow, PyTorch, SQL, HTML — none of these are needed. Every minute spent outside this curriculum is a minute wasted before November 7.

---

*Team Ergon — NAPE AICE 2026 Hackathon | Eko Hotel & Suites, Lagos, November 7–8*
