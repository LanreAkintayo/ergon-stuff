# 🏆 The Exact Norsk Hydro Core Log Practice Pack: Grandmaster Playbook (All 23 Files)

This practice pack is a **pixel-perfect replica of the authentic 1980s Norsk Hydro 1:200 Core Log dataset** from the Norwegian Offshore Directorate (SODIR) demonstrated in your hackathon.

It contains **23 complete test PDFs** covering every real-world trap and scanning anomaly your team will encounter during the competition.

---

## 📂 Complete Practice Pack Roster (`norsk_hydro_practice_pack/`)

### Phase 1: Baseline DPI & Orientation Calibration (Files 01 – 10)
| File Name | Orientation | Resolution | Well Name | Unique Practice Challenge |
| :--- | :--- | :--- | :--- | :--- |
| **[`WB_..._ENCL_1.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_1.pdf)** | Portrait | 150 DPI | `6406/3-2` | Baseline calibration. 11 cores. Special recovery notation `98 (+2)`. |
| **[`WB_..._ENCL_2.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_2.pdf)** | Portrait | 200 DPI | `6406/3-3` | Higher pixel density. Blank recovery column (tests null handling). |
| **[`WB_..._ENCL_3.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_3.pdf)** | Landscape | 150 DPI | `6407/1-3` | **Horizontal layout**. Coordinates differ from portrait! "Poor Quality Original" stamp. |
| **[`WB_..._ENCL_4.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_4.pdf)** | Portrait | **100 DPI** | `6506/12-4` | **Low resolution / fax blur**. Tests AI OCR clarity on small characters. |
| **[`WB_..._ENCL_5.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_5.pdf)** | Sideways (90°) | 200 DPI | `6407/2-2` | **The Sideways Scanner Trap!** Must be auto-rotated 90° before cropping. |
| **[`WB_..._ENCL_6.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_6.pdf)** | Portrait | **300 DPI** | `6407/9-1` | **Heavy Archival Scan**. 8.7 megapixels! Fixed pixel crops will slice the wrong area. |
| **[`WB_..._ENCL_7.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_7.pdf)** | Landscape | 120 DPI | `6507/7-1` | Horizontal with low DPI. Decimal depths (`2450.0 - 2468.2`). |
| **[`WB_..._ENCL_8.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_8.pdf)** | Portrait | 150 DPI | `6406/2-1` | 1.5° scanner tilt. 8 core intervals. Exactly matches demo file! |
| **[`WB_..._ENCL_9.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_9.pdf)** | Sideways (90°) | 150 DPI | `6506/11-1` | Sideways feed + low contrast. Exactly matches demo file! |
| **[`WB_..._ENCL_10.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_10.pdf)** | Portrait | 200 DPI | `6407/6-1` | 10 dense consecutive core rows. |

### Phase 2: Inconsistent Heights & Vertical Shifts (Files 11 – 14)
| File Name | Orientation | Resolution | Well Name | Unique Practice Challenge |
| :--- | :--- | :--- | :--- | :--- |
| **[`WB_..._ENCL_11.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_11.pdf)** | Portrait | 150 DPI | `6507/8-1` | **Tall 16-Row Table**. Table extends past 40% height. Fixed bottom crops will cut off cores 11-16! |
| **[`WB_..._ENCL_12.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_12.pdf)** | Portrait | 200 DPI | `6406/1-1` | **Vertical Glass Margin Shift**. The entire sheet is shifted down by 80px. Top crop must flex downward. |
| **[`WB_..._ENCL_13.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_13.pdf)** | Portrait | 150 DPI | `6406/2-2` | **Header Bloat**. Multi-line formation and partner list expands header height and pushes table down. |
| **[`WB_..._ENCL_14.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_14.pdf)** | Portrait | 120 DPI | `6506/12-1` | **Compact Short Sheet (85% height)**. Tight margins; header starts immediately at top edge. |

### Phase 3: Landscape Centered Sheets (Files 15 – 16)
| File Name | Orientation | Resolution | Well Name | Unique Practice Challenge |
| :--- | :--- | :--- | :--- | :--- |
| **[`WB_..._ENCL_15.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_15.pdf)** | Landscape | 150 DPI | `6406/2-3` | **Wide Horizontal Banner Section**. The entire core log block is a wide horizontal banner centered vertically in the middle of the sheet (empty margins above & below). |
| **[`WB_..._ENCL_16.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_16.pdf)** | Landscape | 200 DPI | `6406/1-2` | **Transposed Horizontal Core Table**. Instead of vertical rows, cores run horizontally across columns (Row 1: Core Numbers, Row 2: Intervals, Row 3: Recoveries) centered on the page! |

### Phase 4: Multi-Page Scan Traps (Files 17 – 18)
| File Name | Total Pages | Target Page | Well Name | Unique Practice Challenge |
| :--- | :--- | :--- | :--- | :--- |
| **[`WB_..._ENCL_17.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_17.pdf)** | 2 Pages | **Page 2** | `6407/7-2` | **Page 1 is a Drilling Report Cover**. The actual Norsk Hydro core log is on Page 2! |
| **[`WB_..._ENCL_18.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_18.pdf)** | 3 Pages | **Page 3** | `6506/12-3` | **Pages 1 & 2 are Mud Logs & Bit Summaries**. Target table is hidden on Page 3! |

### Phase 5: Elite Hackathon Curveballs (Files 19 – 23)
| File Name | Orientation | Resolution | Well Name | Unique Practice Challenge |
| :--- | :--- | :--- | :--- | :--- |
| **[`WB_..._ENCL_19.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_19.pdf)** | Portrait | 150 DPI | `6407/7-1` | **Split-Column Table**. Cores 1–7 are on the left, Cores 8–14 are on the right side of the same box! |
| **[`WB_..._ENCL_20.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_20.pdf)** | Portrait | 200 DPI | `6406/3-1` | **Handwritten Pen Corrections**. Typed numbers crossed out with blue ink and hand-corrected! |
| **[`WB_..._ENCL_21.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_21.pdf)** | Portrait | 150 DPI | `6407/1-2` | **Microfiche Negative**. Black background with white glowing letters. Must be inverted before OCR. |
| **[`WB_..._ENCL_22.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_22.pdf)** | Portrait | 150 DPI | `6507/7-2` | **Borderless / Frameless Table**. Tab-spaced typewriter text without black grid borders. |
| **[`WB_..._ENCL_23.pdf`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_23.pdf)** | Portrait | 150 DPI | `6407/9-2` | **180° Inverted Scan**. Fed upside down into scanner. Must be rotated 180° before processing. |

---

## 🎯 Ground Truth Answer Keys Included

1. [`ground_truth_cores.csv`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/ground_truth_cores.csv): Contains **154 individual core interval rows** across all 23 wells:
   - `well_name`, `source_file`, `target_page`, `core_no`, `top_depth_m`, `bottom_depth_m`, `recovery_pct`, `group_formation`
2. [`ground_truth_metadata.csv`](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/norsk_hydro_practice_pack/ground_truth_metadata.csv): Contains all **23 well header records**:
   - `well_name`, `source_file`, `target_page`, `date`, `licence`, `field`, `owners`, `water_depth`, `total_depth_logger`, `formation_at_td`

---

## 💡 Hackathon Code Recipes: How to Crack Every Trap

### 0. Natural Sorting of Enclosure Files (`ENCL_1` to `ENCL_23`)
Python's standard alphabetical `sorted()` sorts `ENCL_10` before `ENCL_2`. Use natural regex sorting:
```python
import os, re

def sort_enclosure_files(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
    # Extract integer after ENCL_ and sort numerically:
    return sorted(files, key=lambda f: int(re.search(r'ENCL_(\d+)', f).group(1)))
```

### 1. Multi-Page Trap (Files 17 & 18): Finding the Real Core Log Page
Never assume page 1 is the core log. Iterate through pages and search for keyword anchors:
```python
import fitz # PyMuPDF

def find_core_log_page(pdf_path):
    doc = fitz.open(pdf_path)
    for page_idx, page in enumerate(doc):
        text = page.get_text().upper()
        # Key anchors on Norsk Hydro Core Logs:
        if "CORE LOG" in text or "CORES DESCRIBED" in text or "NORSK HYDRO" in text:
            return page_idx # 0-indexed
    return 0 # Fallback to page 1
```

### 2. Microfiche Negative Inversion (File 21)
Detect if the image is predominantly dark, and invert it so OCR models can read it:
```python
from PIL import Image, ImageOps, ImageStat

def auto_invert_negative(image):
    grayscale = image.convert("L")
    stat = ImageStat.Stat(grayscale)
    avg_brightness = stat.mean[0]
    if avg_brightness < 100: # Mostly black background
        print("Detected microfiche negative scan! Inverting colors...")
        return ImageOps.invert(image.convert("RGB"))
    return image
```

### 3. Dynamic Bounding Box: Solving Inconsistent Heights (Files 11 – 16)
Instead of a fixed bottom coordinate, use a generous relative window that captures tall tables (16 cores) and centered tables:
```python
def crop_core_table_robust(img, is_landscape=False, is_centered=False):
    w, h = img.size
    if is_centered:
        # Centered landscape sheet (Files 15 & 16)
        return img.crop((int(w * 0.45), int(h * 0.28), int(w * 0.85), int(h * 0.65)))
    elif is_landscape:
        # Standard landscape sheet (Files 03 & 07)
        return img.crop((int(w * 0.45), int(h * 0.12), int(w * 0.85), int(h * 0.48)))
    else:
        # Standard portrait sheet: 48% to 88% width, 12% to 48% height to catch 16 rows!
        return img.crop((int(w * 0.48), int(h * 0.12), int(w * 0.88), int(h * 0.48)))
```

### 4. Split-Column Prompting (File 19)
Give Gemini this instruction in your prompt:
> *"Notice: Some logs display core intervals in side-by-side split columns (e.g., Cores 1 to 7 on the left and Cores 8 to 14 on the right within the same box). Read both columns sequentially from Core 1 through the final core."*

### 5. Handwritten Corrections Prompting (File 20)
> *"Notice: If any typed numbers are struck through with pen and replaced with handwritten numbers above or beside them, always record the handwritten correction as the authoritative value."*

### 6. Transposed Horizontal Table Prompting (File 16)
Standard OCR models often assume tables have vertical columns (`Core | Interval | Recovery`). For transposed tables, prompt Gemini:
> *"Notice: If the core table is arranged horizontally where rows represent properties (Row 1 = Core Numbers, Row 2 = Intervals, Row 3 = Recovery) and columns represent individual cores from left to right, read the table horizontally column-by-column to extract each core row into the standard schema."*


