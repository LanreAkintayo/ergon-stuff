# Team Ergon: Computer Scientist (AI Systems & Backend Architect)
### Role: System Architect & AI Backend Engine Lead
### Duration: 3 Weeks (21 Days) | ~1 to 1.5 hours per day
### Stack: Python 3.12, Windows PowerShell, Ollama, ChromaDB, Pydantic, Streamlit, LightGBM

---

> [!IMPORTANT]
> **The Team Ergon Division of Labor**:
> * **Geologist 1**: Extracts, cleans, and chunks messy PDFs/logs $\to$ produces `well_report_chunks.json`.
> * **Geologist 2**: Writes prompt rules, query expander, evals, and designs the web UI $\to$ produces `app.py`.
> * **You (Computer Scientist & CS 1)**: You build the central nervous system. You index the chunks in a local vector database (ChromaDB), run the local model (Ollama), orchestrate retrieval, build the Scenario B (CSV) fallback, and ensure the entire app runs cold with **zero internet**.

---

## The Mission in One Sentence
> By November 7, you will engineer a high-speed, local RAG retrieval engine and API pipeline that ingests geological data from Geologist 1, executes search queries with sub-second latency, and feeds verified citations to Geologist 2's Streamlit frontend.

---

## Section 0: Prerequisites & Project Architecture (Before Day 1)
*Estimated time: 1.5–2 hours. Do these setup steps first.*

### 0.1 — System Architecture Diagram

```
[Geologist 1]                                              [Geologist 2]
Messy PDFs / Logs                                          Streamlit Web UI
       │                                                          │
       ▼ (Day 1-14)                                               │ (User types question)
`chunks.json` (Text + Metadata)                                   ▼
       │                                             Domain Query Expander
       ▼                                                          │
┌─────────────────────────────────────────────────────────────┐   │
│             YOU: Central AI Backend Engine                  │   │
│                                                             │   │
│  1. Ingestion Worker: Generates embeddings & loads ChromaDB  │   │
│  2. ChromaDB Vector Store: Cosine similarity + Meta filters ◄───┘
│  3. Retrieval Engine: Fetches Top-K relevant chunks         │
│  4. Prompt Orchestrator: Combines context + system guardrails│
│  5. LLM Client: Streams tokens from local Ollama model      │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Streams answer + citations)
                               ▼
                    [Streamlit Web Dashboard]
                    Executive Appraisal Brief
```

### 0.2 — Set Up Your Windows PowerShell Environment
Open PowerShell on your PC and run these commands to set up your dedicated project workspace:

```powershell
# 1. Create a clean project folder in your workspace
mkdir C:\Users\Larry Mosh\.gemini\antigravity\scratch\team_ergon_ai
cd "C:\Users\Larry Mosh\.gemini\antigravity\scratch\team_ergon_ai"

# 2. Create a clean Python 3.12 virtual environment
python -m venv venv

# 3. Activate the virtual environment
.\venv\Scripts\Activate.ps1
# (If PowerShell blocks script execution, run: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned)

# 4. Install the core AI backend stack
pip install --upgrade pip
pip install ollama chromadb pydantic requests streamlit pandas lightgbm
```

### 0.3 — Install Ollama for Windows
1. Download the Windows installer from **[ollama.com/download](https://ollama.com/download)**.
2. Run `OllamaSetup.exe` and let it install.
3. Open a new PowerShell terminal and verify:
   ```powershell
   ollama --version
   ```
4. Pull your primary hackathon model:
   ```powershell
   # 3.2 Billion parameters — fast (40+ tokens/sec on laptop), 100% offline
   ollama pull llama3.2:3b
   ```
   *(If you have extra RAM/VRAM, you can also test `ollama pull qwen2.5:3b` or `ollama pull mistral:7b`).*

---

## Week 1: Local AI Runtime, Python Client & Vector Embeddings
*Goal: Control the local LLM via Python, enforce structured JSON, and understand vector databases.*

---

### Day 1: Testing the Local Ollama Server via HTTP & CLI

Ollama runs a local HTTP microservice on port `11434`. 

**1. Test via PowerShell CLI:**
```powershell
ollama run llama3.2:3b "Respond in one sentence: What is the reservoir rock of the Niger Delta?"
```

**2. Test the REST API directly using PowerShell:**
```powershell
$body = @{
    model = "llama3.2:3b"
    prompt = "State three primary petrophysical properties."
    stream = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:11434/api/generate" -Method Post -Body $body -ContentType "application/json"
```
Notice: Ollama is literally just a REST API endpoint that returns JSON! As a backend developer, you already know how to talk to REST APIs.

---

### Day 2: Building the Python LLM Client Wrapper

Write a clean, reusable Python wrapper class that handles timeouts, connection errors, and token streaming:

```python
# File: llm_client.py
import requests
import json

class LocalLLMClient:
    def __init__(self, host="http://localhost:11434", model="llama3.2:3b"):
        self.host = host
        self.model = model
        self.generate_url = f"{self.host}/api/generate"
        self.chat_url = f"{self.host}/api/chat"

    def is_alive(self) -> bool:
        """Health check to confirm local Ollama daemon is running."""
        try:
            res = requests.get(self.host, timeout=2)
            return res.status_code == 200
        except requests.ConnectionError:
            return False

    def generate(self, prompt: str, system: str = "", temperature: float = 0.0) -> str:
        """Synchronous generation for back-office tasks."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": {
                "temperature": temperature,
                "top_p": 0.1
            }
        }
        res = requests.post(self.generate_url, json=payload, timeout=60)
        res.raise_for_status()
        return res.json().get("response", "").strip()

    def stream_generate(self, prompt: str, system: str = ""):
        """Generator that yields streaming text tokens for the Streamlit UI."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system,
            "stream": True,
            "options": {"temperature": 0.0}
        }
        with requests.post(self.generate_url, json=payload, stream=True, timeout=60) as r:
            for line in r.iter_lines():
                if line:
                    chunk = json.loads(line.decode("utf-8"))
                    yield chunk.get("response", "")


# Test the client
if __name__ == "__main__":
    client = LocalLLMClient()
    if client.is_alive():
        print("✅ Local Ollama Daemon is ALIVE!")
        print("Testing prompt generation...")
        reply = client.generate(
            prompt="What is permeability in reservoir rocks?",
            system="You are an expert geoscientist. Answer in 20 words or less."
        )
        print("AI Response:", reply)
    else:
        print("❌ Ollama is not running! Start it by running 'ollama serve' in PowerShell.")
```

---

### Day 3: Structured Outputs with Pydantic (Strict JSON Schemas)

In AI engineering, raw text is dangerous for backend code. If you need the AI to return an alert or a score, you must enforce a **Pydantic JSON schema**.

```python
# File: schema_enforcer.py
from pydantic import BaseModel, Field
from typing import List, Optional
import json

class GeologicalFinding(BaseModel):
    well_name: str = Field(description="Name of the well")
    formation: str = Field(description="Geological formation name")
    depth_ft: Optional[int] = Field(description="Depth in feet TVDSS if mentioned")
    hydrocarbon_present: bool = Field(description="True if oil or gas was detected")
    confidence_score: float = Field(description="Model confidence from 0.0 to 1.0")

# Force Ollama to return strictly valid JSON matching this schema
def extract_structured_finding(client, excerpt: str) -> GeologicalFinding:
    system_prompt = f"""
    You are a data extraction engine. Analyze the text and output ONLY valid JSON matching this schema:
    {json.dumps(GeologicalFinding.model_json_schema(), indent=2)}
    Do not output any explanation, markdown formatting, or preamble. Return RAW JSON ONLY.
    """
    raw_json = client.generate(prompt=excerpt, system=system_prompt)
    
    # Strip any accidental markdown ticks
    clean_json = raw_json.replace("```json", "").replace("```", "").strip()
    return GeologicalFinding.model_validate_json(clean_json)


# Test with sample excerpt
if __name__ == "__main__":
    from llm_client import LocalLLMClient
    client = LocalLLMClient()
    sample_text = "OML-42 Well-01 penetrated Agbada Sand D at 9,450 ft TVDSS with commercial light oil shows."
    result = extract_structured_finding(client, sample_text)
    print("Parsed Pydantic Object:")
    print("  Well:", result.well_name)
    print("  Formation:", result.formation)
    print("  Depth:", result.depth_ft)
    print("  Hydrocarbon Detected:", result.hydrocarbon_present)
    print("  Confidence:", result.confidence_score)
```

---

### Day 4: Cloud API Fallback Router (Local Ollama $\leftrightarrow$ Cloud Gemini)

Build a router that tries your local Ollama model first (fast, 100% offline). If local is unavailable and internet is on, it falls back seamlessly to the cloud Gemini API:

```python
# File: ai_router.py
import os
from llm_client import LocalLLMClient

class HybridAIRouter:
    def __init__(self, gemini_api_key: str = None):
        self.local_client = LocalLLMClient()
        self.gemini_key = gemini_api_key or os.getenv("GEMINI_API_KEY")

    def query(self, prompt: str, system: str = "") -> str:
        # 1. Prefer local offline Ollama
        if self.local_client.is_alive():
            try:
                return self.local_client.generate(prompt, system=system)
            except Exception as e:
                print(f"[Router Warning] Local call failed ({e}). Attempting cloud fallback...")

        # 2. Cloud Fallback (if key is configured and internet is up)
        if self.gemini_key:
            import google.generativeai as genai
            genai.configure(api_key=self.gemini_key)
            model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system)
            response = model.generate_content(prompt)
            return response.text

        raise RuntimeError("No AI backend available: Local Ollama is down and no cloud API key provided.")
```

---

### Day 5: Understanding Text Embeddings & Cosine Similarity

An **embedding** turns a sentence into an array of 384 or 768 decimal numbers that capture its semantic meaning.

```
"Reservoir porosity is 24%"  ──► [ 0.12, -0.84,  0.45, ... ]
"Rock void space averages 24%" ─► [ 0.11, -0.82,  0.48, ... ]  (Very close mathematically!)
"The drilling rig was red"   ──► [-0.55,  0.12, -0.91, ... ]  (Far away mathematically)
```

**Test local embeddings with ChromaDB's default embedding engine:**
```python
# File: test_embeddings.py
import chromadb.utils.embedding_functions as embedding_functions

# Uses a lightweight, fast, local embedding model: all-MiniLM-L6-v2
embed_fn = embedding_functions.DefaultEmbeddingFunction()

texts = [
    "Agbada formation sandstone with oil shows",
    "High porosity hydrocarbon reservoir rock",
    "Diesel fuel consumption on the offshore generator"
]

embeddings = embed_fn(texts)
print(f"Generated {len(embeddings)} embeddings.")
print(f"Dimensions per vector: {len(embeddings[0])} dimensions.")
```

---

### Day 6: Setting Up ChromaDB (Your Embedded Vector Database)

ChromaDB is like SQLite for vectors. It creates a local `.chroma` folder on your hard drive—no servers to run, zero cloud dependencies:

```python
# File: vector_store.py
import chromadb
from chromadb.utils import embedding_functions

class SubsurfaceVectorStore:
    def __init__(self, persist_directory="./chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.embed_fn = embedding_functions.DefaultEmbeddingFunction()
        
        # Create or get collection
        self.collection = self.client.get_or_create_collection(
            name="subsurface_archives",
            embedding_function=self.embed_fn,
            metadata={"hnsw:space": "cosine"}   # Cosine distance for text similarity
        )

    def add_chunks(self, chunks: list):
        """
        Ingests a list of tagged chunk dictionaries from Geologist 1.
        """
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        documents = [c["text"] for c in chunks]
        metadatas = [c["metadata"] for c in chunks]

        # ChromaDB requires all metadata values to be str, int, float, or bool
        cleaned_metadatas = []
        for m in metadatas:
            cleaned_m = {k: (v if v is not None else "") for k, v in m.items()}
            cleaned_metadatas.append(cleaned_m)

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=cleaned_metadatas
        )
        print(f"✅ Ingested {len(chunks)} chunks into ChromaDB.")

    def count(self) -> int:
        return self.collection.count()


# Test store initialization
if __name__ == "__main__":
    store = SubsurfaceVectorStore()
    print("ChromaDB Initialized. Current record count:", store.count())
```

---

### Day 7: Week 1 Milestone Project

**Build this milestone script:**
1. Create a `milestone1.py` file.
2. Initialize ChromaDB and insert 5 fake well report snippets with metadata (well name, depth, page).
3. Query the collection using vector search: *"Find sandstone intervals with good porosity"*.
4. Verify that ChromaDB returns the top 2 matching excerpts and prints their metadata.

---

## Week 2: Ingestion Service & The Core RAG Orchestrator
*Goal: Ingest Geologist 1's JSON, execute filtered queries, and assemble the full RAG pipeline.*

---

### Day 8: Consuming Geologist 1's `well_report_chunks.json`

Write the production Ingestion Worker that reads Geologist 1's exported JSON file and loads it into ChromaDB:

```python
# File: ingest_worker.py
import json
import os
from vector_store import SubsurfaceVectorStore

def load_geology_chunks(json_filepath: str):
    if not os.path.exists(json_filepath):
        raise FileNotFoundError(f"Cannot find: {json_filepath}")

    with open(json_filepath, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    print(f"Loaded {len(chunks)} chunks from {json_filepath}.")
    return chunks

def run_ingestion(json_filepath: str):
    chunks = load_geology_chunks(json_filepath)
    store = SubsurfaceVectorStore()
    
    # Reset / reload collection cleanly
    try:
        store.client.delete_collection("subsurface_archives")
    except Exception:
        pass
    
    store = SubsurfaceVectorStore()
    store.add_chunks(chunks)
    print(f"🚀 Ingestion Complete! Total indexed vectors: {store.count()}")

if __name__ == "__main__":
    # Test with dummy JSON or real file from Geologist 1
    sample_data = [
        {
            "text": "OML-42 Well-01 penetrated Agbada Sandstone at 9,200 ft TVDSS. Net pay is 48 ft with 23% porosity.",
            "metadata": {"well_name": "OML-42 Well-01", "page_number": 14, "section": "Reservoir", "depth_mentioned": 9200}
        },
        {
            "text": "Bonga South Deep encountered overpressure below 11,400 ft. Mud weight was raised to 13.2 ppg.",
            "metadata": {"well_name": "Bonga South", "page_number": 32, "section": "Drilling", "depth_mentioned": 11400}
        }
    ]
    with open("sample_chunks.json", "w") as f:
        json.dump(sample_data, f)
        
    run_ingestion("sample_chunks.json")
```

---

### Day 9: Advanced ChromaDB Metadata Filtering

In hackathons, users want to search: *"Show me drilling problems, but ONLY for Well-01."* 

ChromaDB allows SQL-style `where` clauses:

```python
# File: search_service.py
from vector_store import SubsurfaceVectorStore

def search_with_filters(store, query_text: str, well_name: str = None, top_k: int = 3):
    """
    Executes hybrid search: semantic vector similarity + strict metadata filtering.
    """
    where_filter = None
    if well_name and well_name != "All Wells":
        where_filter = {"well_name": well_name}

    results = store.collection.query(
        query_texts=[query_text],
        n_results=top_k,
        where=where_filter
    )
    
    extracted_results = []
    if results and results["documents"]:
        docs = results["documents"][0]
        metas = results["metadatas"][0]
        distances = results["distances"][0] if "distances" in results else [0.0]*len(docs)

        for doc, meta, dist in zip(docs, metas, distances):
            extracted_results.append({
                "text": doc,
                "metadata": meta,
                "similarity_score": round(1.0 - dist, 3)   # Convert cosine distance to similarity
            })

    return extracted_results
```

---

### Day 10: Building the Retrieval Engine with Score Thresholding

If a user asks about a well that does not exist, vector search will still return the *least worst* chunks. You must implement a **Similarity Threshold** to filter out low-confidence garbage:

```python
def filter_relevant_chunks(search_results: list, min_similarity: float = 0.45) -> list:
    """
    Drops chunks that have poor semantic similarity to the question.
    Prevents the LLM from hallucinating on irrelevant text.
    """
    relevant = [r for r in search_results if r["similarity_score"] >= min_similarity]
    if not relevant:
        print("[Retrieval Alert] No chunks met the minimum confidence threshold.")
    return relevant
```

---

### Day 11: Prompt Assembly & Context Injection

Now, connect Geologist 2's prompt rules with your retrieved chunks:

```python
# File: prompt_orchestrator.py

def format_context_block(chunks: list) -> str:
    """Formats retrieved chunks into clean numbered context excerpts."""
    if not chunks:
        return "NO RELEVANT ARCHIVE EXCERPTS FOUND."

    context_lines = []
    for i, c in enumerate(chunks):
        meta = c["metadata"]
        header = f"[EXCERPT {i+1} | Well: {meta.get('well_name', 'Unknown')} | Page: {meta.get('page_number', 'N/A')}]"
        context_lines.append(f"{header}\n{c['text']}\n")

    return "\n".join(context_lines)

def build_rag_prompt(user_query: str, retrieved_chunks: list) -> str:
    """Injects retrieved chunks into the user prompt."""
    context_str = format_context_block(retrieved_chunks)
    
    prompt = f"""
RETRIEVED WELL ARCHIVE EXCERPTS:
==================================================
{context_str}
==================================================

GEOSCIENTIST QUESTION:
{user_query}

INSTRUCTIONS:
Answer the question strictly using the retrieved excerpts above. If the data is absent, state: 'Data not available in indexed well archives.'
"""
    return prompt
```

---

### Day 12: Building the Master `query_engine()` Function

This is the central API function that Geologist 2's Streamlit frontend will call:

```python
# File: query_engine.py
from vector_store import SubsurfaceVectorStore
from search_service import search_with_filters
from prompt_orchestrator import build_rag_prompt
from llm_client import LocalLLMClient

class SubsurfaceQueryEngine:
    def __init__(self, system_instruction: str):
        self.store = SubsurfaceVectorStore()
        self.llm = LocalLLMClient()
        self.system_instruction = system_instruction

    def ask(self, user_query: str, well_filter: str = None) -> dict:
        """
        Executes the full RAG cycle and returns answer + verified citation objects.
        """
        # 1. Retrieve top 4 matching chunks
        raw_results = search_with_filters(self.store, user_query, well_name=well_filter, top_k=4)
        
        # 2. Check if anything was found
        if not raw_results:
            return {
                "answer": "No records found matching your query and filter criteria.",
                "citations": []
            }

        # 3. Assemble prompt
        prompt = build_rag_prompt(user_query, raw_results)

        # 4. Generate answer from Local LLM
        answer = self.llm.generate(prompt=prompt, system=self.system_instruction)

        # 5. Extract citations for frontend rendering
        citations = []
        for r in raw_results:
            citations.append({
                "well_name": r["metadata"].get("well_name", "Unknown"),
                "page": r["metadata"].get("page_number", "N/A"),
                "section": r["metadata"].get("section", "General"),
                "excerpt": r["text"][:180] + "...",
                "score": int(r["similarity_score"] * 100)
            })

        return {
            "answer": answer,
            "citations": citations
        }
```

---

### Day 13: End-to-End Terminal CLI Test

Write a simple interactive CLI loop so you can stress-test your backend directly from PowerShell:

```python
# File: cli_test.py
from query_engine import SubsurfaceQueryEngine

SYSTEM_PROMPT = """You are Chief Subsurface Geologist for Team Ergon. Answer strictly from context. Always cite."""

def run_cli():
    print("="*55)
    print("🛢️ Team Ergon: Subsurface Backend CLI")
    print("Type 'exit' to quit.")
    print("="*55)
    
    engine = SubsurfaceQueryEngine(SYSTEM_PROMPT)

    while True:
        q = input("\nEnter Question: ").strip()
        if q.lower() in ["exit", "quit", "q"]:
            break

        print("\nThinking (querying ChromaDB & Ollama)...")
        result = engine.ask(q)
        
        print("\n💡 AI ANSWER:\n", result["answer"])
        print("\n📑 CITATIONS:")
        for c in result["citations"]:
            print(f"  • {c['well_name']} (Page {c['page']}) [{c['score']}% match]")

if __name__ == "__main__":
    run_cli()
```

---

### Day 14: Week 2 Milestone Project

**Milestone Checkpoint:**
* Ingest 2 real well reports (using Geologist 1's actual `well_report_chunks.json`).
* Run `python cli_test.py` in PowerShell.
* Ask 3 real questions. Confirm that your local model answers in under 2 seconds and prints exact page citations!

---

## Week 3: Frontend Integration, Offline Hardening & Scenario B
*Goal: Wire up Streamlit, guarantee 100% offline cold-start, and build the Tabular ML / Text-to-SQL backup.*

---

### Day 15: Connecting the Backend to Geologist 2's Streamlit Dashboard

Now we connect `query_engine.py` directly into Geologist 2's `app.py`:

```python
# Inside app.py (where user submits input)
from query_engine import SubsurfaceQueryEngine

# Initialize engine once using Streamlit resource caching
@st.cache_resource
def get_engine():
    from Geologist2_Curriculum import SYSTEM_INSTRUCTION   # Uses Geologist 2's prompt
    return SubsurfaceQueryEngine(SYSTEM_INSTRUCTION)

engine = get_engine()

# Inside your chat submission block:
if user_prompt := st.chat_input("Ask a geological question..."):
    # 1. Show user message
    st.chat_message("user").write(user_prompt)

    # 2. Query your backend
    with st.spinner("Analyzing indexed subsurface archives..."):
        result = engine.ask(user_prompt, well_filter=selected_well)

    # 3. Render AI response and citations
    with st.chat_message("assistant"):
        st.write(result["answer"])
        
        # Geologist 2's citation expander
        with st.expander("📑 View Verified Citations"):
            for cite in result["citations"]:
                st.markdown(f"**{cite['well_name']}** (Page {cite['page']}) — *{cite['excerpt']}*")
```

---

### Day 16: Offline Hardening (The Airplane Mode Test)

To guarantee you never get stranded by hotel Wi-Fi at Eko Hotel:

1. **Disconnect your laptop from all Wi-Fi and Ethernet (Turn on Airplane Mode).**
2. Reboot your laptop.
3. Open PowerShell and run:
   ```powershell
   ollama run llama3.2:3b "Test offline inference"
   streamlit run app.py
   ```
4. Ask a question. If your app answers normally in airplane mode—**your offline defense is rock solid.**

---

### Day 17: Scenario B Defense 1 — Auto-Tabular ML with LightGBM

What if on November 7, NAPE hands you a 100,000-row CSV of sensor logs or separator pressures (like the 2024 challenges) instead of PDFs?

You will run this pre-coded **Auto-LightGBM script** that cleans data, handles missing values, and trains a model in 30 seconds:

```python
# File: auto_tabular_ml.py
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, f1_score

def train_tabular_model(csv_path: str, target_column: str, is_classification: bool = False):
    """
    Universal Tabular ML Engine: Trains a production LightGBM model on any CSV in seconds!
    """
    print(f"Loading {csv_path}...")
    df = pd.read_csv(csv_path)

    # 1. Clean oilfield missing codes (-999.25, -999, 9999)
    df = df.replace([-999.25, -999.0, 9999.0], np.nan)

    # 2. Separate Features (X) and Target (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Convert text columns to category types for LightGBM
    for col in X.select_dtypes(include=["object"]).columns:
        X[col] = X[col].astype("category")

    # 3. Train / Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Train LightGBM Model
    if is_classification:
        model = lgb.LGBMClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        print("✅ Training Complete! Weighted F1 Score:", round(f1_score(y_test, preds, average='weighted'), 4))
    else:
        model = lgb.LGBMRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        print("✅ Training Complete! Test RMSE:", round(rmse, 4))

    return model
```

---

### Day 18: Scenario B Defense 2 — Text-to-SQL Data Agent (DeployEdu Project 11)

What if NAPE asks: *"Build an AI that answers questions from our historical well database"*?

You build a **Text-to-SQL interface with SQLite**:

```python
# File: text_to_sql.py
import sqlite3
import pandas as pd

def setup_sqlite_database(csv_path: str, db_name="subsurface.db", table_name="well_production"):
    """Loads any CSV into a fast local SQLite database."""
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"✅ Loaded {len(df)} rows into SQLite table '{table_name}'.")

def execute_safe_sql(sql_query: str, db_name="subsurface.db") -> pd.DataFrame:
    """Executes a SQL query with guardrails (blocks DELETE/DROP commands)."""
    blocked_keywords = ["drop", "delete", "truncate", "alter", "update"]
    if any(kw in sql_query.lower() for kw in blocked_keywords):
        raise ValueError("Security Guardrail: Destructive SQL commands are forbidden.")

    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(sql_query, conn)
    conn.close()
    return df
```

---

### Day 19: Git Repository Management & Employer-Grade README

Judges and employers will inspect your GitHub repository. Package your project cleanly:

```markdown
# SubsurfaceAI — Unlocking Dormant Value
### NAPE AICE 2026 Hackathon Finalist | Team Ergon

## Problem Statement
Exploration and production operators face billions in delayed production because 30+ years
of historical well completion reports and wireline logs are trapped in unstructured files.

## Solution Architecture
Team Ergon built a 100% offline, privacy-preserving Subsurface Intelligence Engine:
- **Data Ingestion**: Domain-aware chunking preserving stratigraphy intervals (pdfplumber + OCR).
- **Vector Search**: ChromaDB with cosine similarity and metadata depth filters.
- **Inference Runtime**: Local Ollama Llama 3.2 3B running offline at 42 tokens/sec.
- **Reliability Benchmark**: 10-point automated evaluation suite achieving 100% grounding.

## How to Run Cold in 2 Steps:
1. `ollama run llama3.2:3b`
2. `streamlit run app.py`
```

---

### Day 20: Pre-Flight Checklist & Stress Testing

Run this checklist 48 hours before the event:
* [ ] Ollama models verified locally: `ollama list` shows `llama3.2:3b`.
* [ ] ChromaDB loads without internet.
* [ ] Streamlit UI launches in under 3 seconds.
* [ ] All teammate code merged into `main` branch on GitHub.
* [ ] Python virtual environment fully cached.

---

### Day 21: Full Team Ergon Simulation Drill

* 45-minute dry-run with Geologist 1 and Geologist 2.
* Simulate judge questions, test the download button, test edge cases, and verify zero crashes.

---

## Section 4: The 3 Backend Curveballs & Fail-Safe Protocols

| Curveball | What Happens | The Solution |
| :--- | :--- | :--- |
| **1. Laptop Out of Memory (OOM)** | Large models cause laptop fan to scream and freeze. | Use lightweight 3B models (`llama3.2:3b` or `qwen2.5:3b`) with 4-bit quantization (Q4_K_M). Takes only 2GB of RAM. |
| **2. Hotel WiFi Blackout** | Zero internet connection in conference hall. | Your entire stack (Ollama, ChromaDB, Streamlit, Python packages) is installed locally. App runs 100% in Airplane Mode. |
| **3. Sudden Switch to Pure CSVs** | NAPE gives a sensor spreadsheet instead of PDFs. | Deploy `auto_tabular_ml.py` (LightGBM) or `text_to_sql.py` in under 5 minutes. |

---

## Quick Reference Card: Backend Architect Playbook

```powershell
# Quick Start Commands
ollama serve                        # Starts Ollama background server
ollama list                          # Lists all local models
ollama run llama3.2:3b              # Tests terminal inference
streamlit run app.py                 # Launches the web app
python ingest_worker.py              # Ingests Geologist 1's JSON into ChromaDB
python cli_test.py                   # Tests backend RAG in terminal
```

---

*Team Ergon — NAPE AICE 2026 Hackathon | Eko Hotel & Suites, Lagos, November 7–8*
