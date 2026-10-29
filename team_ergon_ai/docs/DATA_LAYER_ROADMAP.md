# 🚀 Team Ergon: Data Layer Mastery Roadmap
> **Goal:** Master the end-to-end pipeline from messy subsurface PDFs to clean CSV tables, smart RAG chunks, and ChromaDB search. Designed for Jupyter Notebooks, Google Colab, and local hackathon execution.

---

## 🗺️ The High-Level Flow

```text
[ Raw Scans / PDFs ]
        │
        ▼
[ Phase 1: Cleaning & Extraction ]
        │
        ├─► Deliverable 1: final_cores.csv     (All core intervals across wells)
        └─► Deliverable 2: final_metadata.csv  (1 identity row per well)
        │
        ▼
[ Phase 2: Domain-Aware Chunking ]
        │
        └─► Deliverable 3: clean_chunks.json   (Sentences + Metadata tags)
        │
        ▼
[ Phase 3: ChromaDB Vector Store ]
        │
        └─► Ingested via ingest_worker.py      (Subsurface semantic search ready!)
```

---

## 📋 Step-by-Step Action Plan

### ✅ Phase 1: Environment & Notebook Readiness
- [x] Install `ipykernel` in `team_ergon_ai/venv` *(Done!)*
- [ ] Create a starter notebook `data_layer_pipeline.ipynb` in `team_ergon_ai/`
- [ ] Verify kernel connection: run a quick `import pandas as pd`, `import chromadb` test cell.

---

### 🧪 Phase 2: Master Deliverable 1 (`final_cores.csv`)
*Objective: Extract, clean, and concatenate core intervals from well documents.*

- [ ] **Step 2.1: Inspect Raw Data & Traps**
  - Fused columns (e.g. `"3930 - 3934"` split into `top_depth_m` and `bottom_depth_m`).
  - European decimal commas (`73,5` $\rightarrow$ `73.5`).
  - Symbol & unit cleanup (`%`, `m`, `(+2)`).
- [ ] **Step 2.2: Apply Domain Validation Rules**
  - Ensure `bottom_depth_m > top_depth_m`.
  - Ensure `0 <= recovery_pct <= 100.0`.
  - Replace corrupt sensor values (`-999.25` $\rightarrow$ `NaN`).
- [ ] **Step 2.3: Concatenate Fleet Tables**
  - Combine individual well tables into one unified `final_cores.csv`.
  - Ensure columns: `well_name`, `source_file`, `core_no`, `top_depth_m`, `bottom_depth_m`, `recovery_pct`, `formation`.

---

### 📇 Phase 3: Master Deliverable 2 (`final_metadata.csv`)
*Objective: Build the well "identity card" table (1 clean row per well).*

- [ ] **Step 3.1: Locate Header Information**
  - Handle multi-page documents (ensure we grab the header, not cover page noise).
  - Extract: `well_name`, `licence`, `field`, `owners`, `water_depth`, `total_depth_logger`, `formation_at_td`.
- [ ] **Step 3.2: Sanitize & Export**
  - Strip trailing whitespace and non-standard characters.
  - Export to `final_metadata.csv`.

---

### 🧩 Phase 4: Master Deliverable 3 (`clean_chunks.json`)
*Objective: Turn CSV rows and geological notes into high-semantic text chunks for ChromaDB.*

- [ ] **Step 4.1: Write the 15-Line Chunk Generator**
  - Loop through `final_cores.csv`.
  - Format each row into a natural English sentence:
    `"Well {well_name} Core {core_no} was cut from {top_depth_m}m to {bottom_depth_m}m in {formation} with {recovery_pct}% recovery."`
- [ ] **Step 4.2: Attach Full Metadata**
  - Keep `well_name`, `core_no`, `top_depth_m`, `bottom_depth_m`, `recovery_pct`, `formation` in the `metadata` dictionary.
  - Drop or handle `NaN` values so ChromaDB doesn't throw errors.
- [ ] **Step 4.3: Export to JSON**
  - Save as `clean_chunks.json`.

---

### ⚡ Phase 5: Ingestion into ChromaDB & Query Verification
*Objective: Load chunks into the vector database and prove it works.*

- [ ] **Step 5.1: Run Ingestion Worker**
  - Execute `python ingest_worker.py` (or run it directly from your notebook).
  - Verify chunk count in ChromaDB: `store.count()`.
- [ ] **Step 5.2: Run Test Semantic Queries**
  - Ask: *"What is the recovery for core 1 in well 6406/3-2?"*
  - Test metadata filtering: `store.query(text="high recovery cores", where={"well_name": "6406/3-2"})`.
  - Verify similarity search returns the correct chunks.

---

### 🏆 Phase 6: Hackathon & Colab Readiness
- [ ] Verify the notebook runs end-to-end with **"Restart Kernel & Run All"** without errors.
- [ ] Test importing the `.ipynb` file into Google Colab.
- [ ] Add clean markdown headings and explanatory notes above each code cell so judges can follow along effortlessly.

---

## 💡 Quick Code Cheatsheet

### 1. The 15-Line CSV-to-Chunks Converter:
```python
import pandas as pd
import json

df = pd.read_csv("final_cores.csv")
chunks = []

for _, row in df.iterrows():
    # Build clean sentence
    text = (
        f"Well {row['well_name']} Core {row['core_no']} was retrieved between "
        f"{row['top_depth_m']}m and {row['bottom_depth_m']}m in the {row['formation']} "
        f"formation with a recovery of {row['recovery_pct']}%."
    )
    # Build clean metadata (filtering out NaN)
    metadata = {k: v for k, v in row.to_dict().items() if pd.notna(v)}
    
    chunks.append({
        "chunk_id": f"core_{row['well_name']}_{row['core_no']}",
        "text": text,
        "metadata": metadata
    })

with open("clean_chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=4)
```

### 2. Ingesting into ChromaDB:
```python
from vector_store import SubsurfaceVectorStore
import json

with open("clean_chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

store = SubsurfaceVectorStore()
store.reset()
store.add_chunks(chunks)
print("Active chunks in store:", store.count())
```
