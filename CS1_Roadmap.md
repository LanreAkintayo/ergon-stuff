# CS 1 — The Complete Roadmap to Becoming Unshakeable
## NAPE AICE 2026 Hackathon | Team Ergon Backend Architect
### Start: October 15 → Target: November 6 (23 days available, ~1.5–2 hrs/day)

---

> [!IMPORTANT]
> **How to use this roadmap:**
> - Each checkbox `[ ]` is a skill you need. Mark it `[x]` when you've done it and feel confident.
> - Sections are ordered from foundational → advanced. **Do not skip ahead** — each layer builds on the one before it.
> - The 🔴 icon means **this is a hackathon-critical skill** — you cannot go to Eko Hotel without it.
> - The 🟡 icon means **this gives you an edge** — it separates a "good" team from a winning team.
> - The 🟢 icon means **nice-to-know** — it builds depth but won't block you on November 7.

---

## Progress Dashboard

| Phase | Description | Est. Days | Status |
| :---: | :--- | :---: | :---: |
| **0** | Terminal & Environment Setup | 1 | ✅ |
| **1** | Python Foundations (What the Curriculum Assumes You Know) | 3 | ✅ |
| **2** | Working with External Data (JSON, Files, APIs) | 2 | ✅ |
| **3** | Your Local AI Engine (Ollama) | 2 | ⬜ |
| **4** | Vector Databases & Embeddings (ChromaDB) | 2 | ⬜ |
| **5** | The RAG Pipeline (Your Core Deliverable) | 3 | ⬜ |
| **6** | Scenario B Defenses (Tabular ML & SQL) | 2 | ⬜ |
| **7** | Integration, Offline Hardening & Stress Testing | 2 | ⬜ |
| **8** | Pitch, Git & War Room | 2 | ⬜ |
| **9** | The Final 15% (Messy Data, Muscle Memory, Contract Lock-In & Chaos Drills) | 2 | ⬜ |

**Total estimated: 21 working days out of 23 available → 2 days of buffer.**

---

## Phase 0: Terminal & Environment Setup (Day 1) — COMPLETED ✅
*You conquered the terminal, set up your private sandbox, installed the full 8-tool AI stack, and automated everything with GNU Make.*

### 0.1 — PowerShell & Git Bash Fundamentals
- [x] 🔴 Open Windows PowerShell / Git Bash and understand what it is (a text interface to your computer)
- [x] 🔴 Learn these 8 essential commands and practice each one:
  - `pwd` — "Where am I right now?" (prints your current folder path)
  - `ls` (or `dir`) — "What files are in this folder?"
  - `cd <folder>` — "Move me into this folder"
  - `cd ..` — "Go back up one folder"
  - `mkdir <name>` — "Create a new folder"
  - `cat <filename>` — "Show me what's inside this text file"
  - `cls` (or `clear`) — "Clear the terminal screen"
  - `Ctrl + C` — "STOP whatever is currently running"
- [x] 🔴 Understand what a **file path** is: `C:\Users\Larry Mosh\hackathon-projects\ergon\team_ergon_ai`
- [x] 🟡 Know the difference between **absolute paths** and **relative paths**

### 0.2 — Python Installation & Virtual Environment
- [x] 🔴 Confirm Python 3.12+ is installed: Python 3.12.10 confirmed
- [x] 🔴 Understand what `pip` is (Python's package installer — like an app store for code libraries)
- [x] 🔴 Create and activate a virtual environment:
  ```bash
  cd "c:\Users\Larry Mosh\hackathon-projects\ergon\team_ergon_ai"
  source venv/Scripts/activate
  ```
- [x] 🔴 Understand what a virtual environment is (private sandbox preventing dependency conflicts)
- [x] 🔴 Install the full project stack:
  `chromadb`, `pydantic`, `requests`, `ollama`, `pandas`, `streamlit`, `lightgbm`, `scikit-learn`
- [x] 🔴 Verify installations work with `verify_stack.py` and `make check`
- [x] 🟡 Install GNU Make 4.4.1 and configure automation with [Makefile](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/Makefile) and [run](file:///c:/Users/Larry%20Mosh/hackathon-projects/ergon/team_ergon_ai/run)

### 0.3 — VS Code Setup
- [x] 🔴 Install and configure VS Code
- [x] 🔴 Learn to open integrated terminal
- [x] 🔴 Create and run Python files

### ✅ Phase 0 Checkpoint — PASSED
> Your private sandbox is live. All 8 libraries are installed and tested. You automated your development workflow with `make check`. You are completely ready for Level 1!

---

## Phase 1: Python Foundations (Days 2–4) — COMPLETED ✅
*You conquered the core language by building 5 oilfield data challenges from an empty screen.*

### 1.1 — Variables & Data Types (Day 2)
- [x] 🔴 Understand and create variables: `str`, `int`, `float`, `bool`
- [x] 🔴 Use multiline f-strings to construct summary cards
- [x] 🔴 Perform type casting: `int(raw_depth)` to convert strings to numbers
- [x] 🔴 Verified with `challenge_1.py`

### 1.2 — Lists & Indexing (Day 2)
- [x] 🔴 Create and navigate lists using `[0]` and `[-1]`
- [x] 🔴 Use `len()` to count data stations
- [x] 🔴 Slicing lists: `depths[2:5]` to isolate target reservoir intervals
- [x] 🔴 Appending data: `.append("Akata Shale")`
- [x] 🔴 Verified with `challenge_2.py`

### 1.3 — Dictionaries & Safe Data Access (Day 2)
- [x] 🔴 Create and access key-value pairs (`chunk["well"]`)
- [x] 🔴 Defensive extraction: `chunk.get("operator", default)` to prevent `KeyError` crashes
- [x] 🔴 Dynamic key assignment: `chunk["is_reservoir"] = chunk["porosity"] >= 0.20`
- [x] 🔴 Building verifiable citations
- [x] 🔴 Verified with `challenge_3.py`

### 1.4 — Loops & Compound Conditions (Day 3)
- [x] 🔴 Iterating lists of dictionaries with `for chunk in chunks:`
- [x] 🔴 Filtering with compound `and` conditions: `lithology == "Sandstone" and porosity > 0.2`
- [x] 🔴 Accumulating data and computing statistical aggregates (`sum() / len()`)
- [x] 🔴 Verified with `challenge_4.py`

### 1.5 — Functions & Anti-Hallucination Guards (Day 3)
- [x] 🔴 Defining reusable functions with `def` and parameters
- [x] 🔴 Defensive guard clauses: empty context detection (`if not retrieved_context.strip(): return ...`)
- [x] 🔴 Grounded RAG prompt assembly
- [x] 🔴 Verified with `challenge_5.py`

### ✅ Phase 1 Checkpoint — PASSED 🎉
> You wrote 5 complete Python programs from a completely blank screen without copy-pasting, covering variables, types, lists, slicing, dictionaries, defensive `.get()`, loops, filtering, and functions. You are officially proficient in Python backend fundamentals!

---

## Phase 2: Working with External Data (Days 5–6) — COMPLETED ✅
*Your job is moving data between files, APIs, and databases. You mastered how data flows through files, network requests, dataframes, and schemas.*

### 2.1 — JSON File I/O & In-Memory Operations
- [x] 🔴 Safe file reading with `with open(..., "r", encoding="utf-8")`
- [x] 🔴 Writing formatted JSON with `json.dump(..., indent=4)` — *Tested in `p2_challenge_1.py`*
- [x] 🔴 Defensive file loading with `try / except FileNotFoundError` — *Tested in `p2_challenge_2.py`*
- [x] 🔴 Parsing in-memory API strings with `json.loads()` and `json.dumps()` — *Tested in `p2_challenge_3.py`*

### 2.2 — Pydantic Schema Enforcement (The Bouncer)
- [x] 🔴 OOP Inheritance from `BaseModel`
- [x] 🔴 Strict type annotations and default values
- [x] 🔴 Catching corrupt fields with `try / except ValidationError as e` — *Tested in `p2_challenge_4.py`*
- [x] 🔴 End-to-end ingestion pipeline filtering clean from corrupt chunks — *Tested in `p2_challenge_5.py`*

### 2.3 — Resilient Network Requests (`requests`)
- [x] 🔴 Making HTTP GET & POST calls
- [x] 🔴 Handling status codes (`200 OK`, `405 Method Not Allowed`)
- [x] 🔴 Offline protection: catching `requests.exceptions.ConnectionError` — *Tested in `p2_challenge_6.py`*

### 2.4 — Tabular Data Analysis with Pandas (Scenario B Defense)
- [x] 🔴 Loading and saving CSV files (`pd.read_csv`, `df.to_csv`)
- [x] 🔴 Cleaning oilfield sensor error codes: `df.replace(-999.25, np.nan, inplace=True)`
- [x] 🔴 Calculating statistical metrics: `df["porosity"].mean()`
- [x] 🔴 Boolean mask filtering: `(df["lithology"] == "Sandstone") & (df["porosity"] >= 0.20)`
- [x] 🔴 Exporting filtered tables — *Tested in `p2_challenge_7.py`*

### ✅ Phase 2 Checkpoint — PASSED 🏆
> You can read/write JSON files, validate complex schemas with Pydantic, make resilient HTTP API calls with offline error handling, and manipulate tabular CSV spreadsheets with pandas. You are officially ready to control local AI engines!

---

## Phase 3: Your Local AI Engine — Ollama (Days 7–8)
*This is where it gets real. You are now controlling an actual AI model running on YOUR laptop.*

### 3.1 — Ollama Installation & First Contact (Day 7, ~30 min)
- [x] 🔴 Download and install Ollama: v0.40.4 verified
- [x] 🔴 Verify installation: `ollama --version` in terminal (v0.40.4 confirmed)
- [x] 🔴 Pull your primary model: `ollama pull llama3.2:3b` (2.0 GB verified in memory)
- [x] 🔴 Test it from the terminal and Python: `make llm` generated petrophysical responses
- [x] 🔴 Understand what just happened:
  > The model file is now saved permanently on your hard drive. It does NOT need the internet to run. The `ollama serve` daemon starts automatically when you run any command.
- [ ] 🟡 List all downloaded models: `ollama list`
- [ ] 🟡 Pull a backup model: `ollama pull qwen2.5:3b`

### 3.2 — The Python LLM Client (Day 7, ~45 min)
- [x] 🔴 Build `llm_client.py` — a reusable class that wraps Ollama's HTTP API:
  - `is_alive()` — health check via `GET http://localhost:11434`
  - `generate()` — synchronous prompt → response (for backend tasks)
  - `stream_generate()` — streaming token-by-token (for live UI)
- [x] 🔴 Test the client from terminal: `python llm_client.py` should print `Local Ollama Daemon is alive`
- [x] 🔴 Understand system prompts vs user prompts:
  > **System prompt** = permanent instructions that shape the AI's personality and rules (e.g., "You are a Chief Geoscientist. Only cite provided data.")
  > **User prompt** = the actual question the user types.
- [x] 🔴 Understand `temperature`:
  - `temperature=0.0` → deterministic, same question = same answer every time (what you want for a hackathon)
  - `temperature=0.7` → creative, varied answers (what you do NOT want for geological facts)
- [x] 🟡 Understand `top_p=0.1` — limits the AI to only the most probable words, reduces randomness even further

### 3.3 — Structured Output Extraction (Day 8, ~45 min)
- [x] 🔴 Build `schema_enforcer.py` — forces the AI to return valid JSON matching a Pydantic schema
- [x] 🔴 Understand the technique: you dump the Pydantic schema into the system prompt and tell the AI "Return RAW JSON ONLY"
- [x] 🔴 Handle the common failure: AI wraps its response in markdown ` ```json ... ``` ` — strip those ticks before parsing
- [x] 🔴 Test with a real geological excerpt and verify the Pydantic object has correct field values

### 3.4 — The Cloud Fallback Router (Day 8, ~30 min)
- [x] 🔴 Build `ai_router.py` — tries local Ollama first, falls back to Gemini API if available
- [x] 🔴 Understand the priority chain: Local (fast, offline) → Cloud (backup, needs internet)
- [x] 🟡 Know how to set environment variables in PowerShell: `$env:GEMINI_API_KEY = "your-key-here"`
- [x] 🔴 Test the router with Ollama running → works locally
- [x] 🔴 Test the router with Ollama stopped → falls back to cloud (or throws clear error if no API key)

### 3.5 — Concepts You MUST Understand (Not Code, Just Knowledge) (Day 8, ~15 min)
- [ ] 🔴 What is an LLM? → A prediction engine that guesses the next word based on everything before it. It has NO knowledge of truth.
- [ ] 🔴 What is "hallucination"? → When the AI confidently makes up facts that aren't in the data. This is your #1 enemy.
- [ ] 🔴 What is RAG? → Retrieval-Augmented Generation. Instead of trusting the AI's memory, you FORCE-FEED it relevant documents and say "only answer from these."
- [ ] 🔴 Why local models? → Privacy (NAPE's oilfield data shouldn't be sent to OpenAI), speed (no network latency), and reliability (no Wi-Fi needed).

### ✅ Phase 3 Checkpoint
> You can start Ollama, send it prompts from Python, get structured JSON responses, and understand the difference between a system prompt and a user prompt. You know what RAG is and why hallucination is dangerous.

---

## Phase 4: Vector Databases & Embeddings — ChromaDB (Days 9–10)
*This is the "memory" of your AI. Without this, it has nothing to search.*

### 4.1 — Understanding Embeddings Intuitively (Day 9, ~30 min)
- [x] 🔴 Understand what an embedding is:
  > Every sentence gets converted into a list of ~384 numbers (coordinates). Similar sentences have similar coordinates, like houses in the same neighborhood on a map. "High porosity sandstone" and "good reservoir quality rock" end up in the same neighborhood, even though they use different words.
- [x] 🔴 Test local embeddings with ChromaDB's built-in model:
  ```python
  import chromadb.utils.embedding_functions as ef
  embed_fn = ef.DefaultEmbeddingFunction()
  vectors = embed_fn(["porosity is 24%", "rock pore space is 24%", "the sky is blue"])
  print(len(vectors[0]))  # 384 dimensions
  ```
- [x] 🔴 Understand cosine similarity:
  > Two vectors pointing in the same direction = high similarity (close to 1.0). Two vectors pointing in different directions = low similarity (close to 0.0). The search engine finds the vectors closest to your question's vector.
- [x] 🟡 Know that the embedding model (`all-MiniLM-L6-v2`) is different from the LLM (`llama3.2:3b`) — the embedding model only converts text to numbers, it cannot answer questions

### 4.2 — Setting Up ChromaDB (Day 9, ~45 min)
- [x] 🔴 Build `vector_store.py` — the `SubsurfaceVectorStore` class:
  - `__init__` — creates a persistent local database folder (`./chroma_db`)
  - `add_chunks()` — inserts Geologist 1's text + metadata into the database
  - `count()` — returns how many chunks are stored
- [x] 🔴 Understand `PersistentClient` — data survives even if you restart your laptop (saved to disk, not just RAM)
- [x] 🔴 Understand the collection concept — a collection is like a table in a regular database, but for vectors
- [x] 🔴 Know that metadata values must be `str`, `int`, `float`, or `bool` — no `None`, no nested dicts. Clean your metadata before inserting.
- [x] 🔴 Test: Insert 5 sample chunks, print `store.count()` → should say `5`

### 4.3 — Querying ChromaDB (Day 10, ~45 min)
- [x] 🔴 Build `search_service.py` — the `search_with_filters()` function:
  - Vector similarity search: "find the 3 chunks most similar to this question"
  - Metadata filtering: "but only from Well-01"
- [x] 🔴 Understand `n_results` (top_k): how many results to return
  - `top_k=3` is safe and fast
  - `top_k=5` gives more context but risks including irrelevant chunks
- [x] 🔴 Understand `where` filters — this is how you limit search to a specific well, depth range, or section
- [x] 🔴 Understand cosine distance vs. similarity:
  - ChromaDB returns `distance` (lower = more similar)
  - You convert: `similarity = 1.0 - distance`
  - A similarity of 0.85 means "very relevant", 0.30 means "probably irrelevant"
- [x] 🔴 Build `filter_relevant_chunks()` — drops any results below a minimum similarity threshold (default: 0.45)
  > This is your **anti-hallucination firewall**. If the user asks about a well that doesn't exist in your data, ALL results will have low similarity. Your filter catches this and returns "Data not available" instead of letting the AI make up an answer.

### 4.4 — The Ingestion Worker (Day 10, ~30 min)
- [x] 🔴 Build `ingest_worker.py` — reads Geologist 1's JSON file and loads it into ChromaDB:
  - `load_geology_chunks()` — reads and parses the JSON file
  - `run_ingestion()` — deletes old data, creates fresh collection, inserts new chunks
- [x] 🔴 Test with sample data: create a `sample_chunks.json` with 3–5 entries, run ingestion, verify count
- [x] 🔴 Understand the reload pattern: delete collection → recreate → insert. This ensures no stale data from previous runs.

### ✅ Phase 4 Checkpoint — PASSED 🏆
> You can explain what embeddings and cosine similarity are in plain English. You can insert chunks into ChromaDB, search with filters, apply similarity thresholds, and verify results. You can ingest a JSON file end-to-end.

---

## Phase 5: The RAG Pipeline — Your Core Deliverable (Days 11–13)
*This is the main thing you're building. Everything before this was preparation.*

### 5.1 — Prompt Assembly (Day 11, ~30 min)
- [x] 🔴 Build `prompt_orchestrator.py`:
  - `format_context_block()` — takes retrieved chunks and formats them as numbered excerpts with well/page headers
  - `build_rag_prompt()` — injects formatted context + user question into a structured prompt template
- [x] 🔴 Understand why formatting matters:
  > If you dump raw text into the LLM, it gets confused. Numbered excerpts with clear headers (`[EXCERPT 1 | Well: Well-01 | Page: 14]`) help the AI find and cite the right source.
- [x] 🔴 Include the instruction: "If the data is absent, state: 'Data not available in indexed well archives.'" — this is your hallucination guardrail in the prompt itself

### 5.2 — The Master `query_engine.py` (Day 11, ~45 min)
- [ ] 🔴 Build `SubsurfaceQueryEngine` — the central class that Geologist 2's frontend calls:
  1. Receives user question + optional well filter
  2. Calls `search_with_filters()` to get top matching chunks from ChromaDB
  3. Checks if any results were found — if not, returns a "no data" response
  4. Calls `build_rag_prompt()` to assemble the full prompt
  5. Calls `self.llm.generate()` to get the AI's answer
  6. Extracts citation metadata from the retrieved chunks
  7. Returns `{"answer": "...", "citations": [...]}`
- [ ] 🔴 Understand the return schema:
  ```python
  {
      "answer": "The AI's grounded response text...",
      "citations": [
          {"well_name": "Well-01", "page": 14, "section": "Reservoir", "excerpt": "...", "score": 87}
      ]
  }
  ```
  > This is the **contract** between you and Geologist 2. They build their UI around this exact dictionary shape.
- [ ] 🔴 Know how to adjust `top_k` and `min_similarity` to tune retrieval quality

### 5.3 — CLI End-to-End Test (Day 12, ~45 min)
- [ ] 🔴 Build `cli_test.py` — an interactive terminal chat loop:
  - User types a question → engine processes → answer + citations printed
  - Type `exit` to quit
- [ ] 🔴 Test with at least 5 questions:
  - A straightforward question that SHOULD return good results
  - A question about a well that DOESN'T exist in your data (should say "no data")
  - A question that's vaguely related but not exact (tests similarity matching)
  - A question with no geological relevance at all (should be filtered out)
  - A multi-part question: "Compare porosity of Well-01 and Well-02"
- [ ] 🔴 For each test, observe:
  - Did it retrieve the RIGHT chunks? (Check the citations)
  - Did it answer ONLY from the provided context?
  - How fast was the response? (Should be under 5 seconds)

### 5.4 — Performance Tuning & Debugging (Day 12, ~30 min)
- [ ] 🔴 Know the 3 levers you can pull when answers are wrong:

  | Problem | Likely Cause | Fix |
  | :--- | :--- | :--- |
  | AI gives wrong answer despite having right context | Prompt issue | Improve system prompt wording (coordinate with Geologist 2) |
  | AI gives answer from wrong well/section | Retrieval issue | Lower `top_k`, increase `min_similarity`, add metadata filter |
  | AI says "no data" when data DOES exist | Chunking issue | Geologist 1 needs to re-chunk (chunks might be too large or metadata missing) |

- [ ] 🟡 Add logging so you can see what's happening inside the pipeline:
  ```python
  print(f"[DEBUG] Retrieved {len(results)} chunks. Top score: {results[0]['similarity_score']}")
  ```
- [ ] 🟡 Know how to print the full assembled prompt to verify context injection looks correct

### 5.5 — Connecting to Geologist 2's Streamlit UI (Day 13, ~45 min)
- [ ] 🔴 Understand how Streamlit works at a high level:
  > It's a Python library that turns a `.py` file into a web page. `st.write("Hello")` shows text. `st.chat_input()` creates a chat box. `st.spinner()` shows a loading animation. You write Python, not HTML.
- [ ] 🔴 Know how to expose your `query_engine` to the frontend:
  ```python
  @st.cache_resource
  def get_engine():
      return SubsurfaceQueryEngine(SYSTEM_INSTRUCTION)
  ```
  > `@st.cache_resource` means: "Create the engine ONCE when the app starts, then reuse it for every question." Without this, ChromaDB would reload on every keystroke.
- [ ] 🔴 Run `streamlit run app.py` and test the full loop in the browser
- [ ] 🟡 Know that Streamlit re-runs the entire script from top to bottom on every interaction — that's why caching matters

### 5.6 — Understanding the Data Contract (Day 13, ~15 min)
- [ ] 🔴 Memorize the agreed schema between you and Geologist 1:
  ```json
  {
      "text": "The extracted text content...",
      "metadata": {
          "well_name": "OML-42 Well-01",
          "page_number": 14,
          "section": "Reservoir Description",
          "depth_mentioned": 9200,
          "formation": "Agbada"
      }
  }
  ```
- [ ] 🔴 Know which fields are required (`text`, `well_name`, `page_number`) vs optional (`depth_mentioned`, `formation`, `section`)
- [ ] 🔴 Write a quick validation function that checks Geologist 1's JSON before ingestion (catches errors early)

### ✅ Phase 5 Checkpoint
> You have a fully working RAG pipeline. You type a question in the terminal, ChromaDB retrieves relevant chunks, the local LLM answers strictly from context, and citations are printed. You can also run it through Streamlit in the browser. This is your core deliverable for the hackathon.

---

## Phase 6: Scenario B Defenses (Days 14–15)
*What if NAPE gives you spreadsheets instead of PDFs? You need a backup plan ready to deploy in 10 minutes.*

### 6.1 — Auto-Tabular ML with LightGBM (Day 14, ~45 min)
- [ ] 🔴 Build `auto_tabular_ml.py`:
  - Load any CSV
  - Clean oilfield null codes (-999.25, -999, 9999)
  - Split into train/test sets
  - Train a LightGBM classifier or regressor
  - Print accuracy/RMSE score
- [ ] 🔴 Understand the difference between classification ("Is this rock Shale or Sandstone?") and regression ("Predict the porosity value")
- [ ] 🔴 Understand `train_test_split` — you keep 80% of data for training, 20% for testing. The model never sees test data during training.
- [ ] 🟡 Know how to read a feature importance chart — which input columns matter most for predictions
- [ ] 🟡 Know `sklearn.metrics` — `f1_score` for classification, `mean_squared_error` for regression

### 6.2 — Text-to-SQL with SQLite (Day 15, ~45 min)
- [ ] 🔴 Build `text_to_sql.py`:
  - `setup_sqlite_database()` — loads a CSV into a local SQLite database
  - `execute_safe_sql()` — runs SQL queries with guardrails (blocks DELETE/DROP/ALTER)
- [ ] 🔴 Understand what SQL is:
  > SQL is a language for asking questions about tables. `SELECT well_name, porosity FROM wells WHERE depth > 9000` means "show me well names and porosity values where depth is deeper than 9000 ft."
- [ ] 🔴 Understand the Natural Language → SQL flow:
  1. User asks: "Which wells have porosity above 20%?"
  2. The AI generates: `SELECT well_name, porosity FROM wells WHERE porosity > 0.20`
  3. SQLite executes the query and returns a table
- [ ] 🔴 Know the security guardrail: NEVER let the AI run `DROP TABLE` or `DELETE FROM` — your code blocks these

### 6.3 — Scenario B Quick-Deploy Drill (Day 15, ~30 min)
- [ ] 🔴 Practice this drill: "NAPE just gave us a CSV. Go."
  1. Load CSV with pandas → inspect shape and columns (2 min)
  2. Identify the target column (talk to your geologists) (3 min)
  3. Run `auto_tabular_ml.py` → get a model and accuracy score (5 min)
  4. Total deployment time target: **under 10 minutes**
- [ ] 🟡 Practice the Text-to-SQL variation of the same drill

### ✅ Phase 6 Checkpoint
> If NAPE gives you numbers instead of documents, you can have a trained ML model running in under 10 minutes and a Text-to-SQL interface ready in 5. You have practiced the drill at least twice.

---

## Phase 7: Offline Hardening & Stress Testing (Days 16–17)
*This is where most hackathon teams fail. You will not.*

### 7.1 — The Airplane Mode Test (Day 16, ~30 min)
- [ ] 🔴 Turn on Airplane Mode on your laptop (disable ALL network adapters)
- [ ] 🔴 Reboot your laptop
- [ ] 🔴 Open PowerShell, activate your venv, and run:
  ```powershell
  ollama run llama3.2:3b "Test offline inference"
  ```
- [ ] 🔴 Start Streamlit: `streamlit run app.py`
- [ ] 🔴 Ask 3 questions through the UI — all must work with zero internet
- [ ] 🔴 If anything fails, identify and fix the dependency:
  - Common failure: ChromaDB's embedding model tries to download on first run — run it ONCE with internet first to cache it
  - Common failure: Streamlit tries to phone home — set `STREAMLIT_BROWSER_GATHER_USAGE_STATS=false`

### 7.2 — Cold-Start Speed Test (Day 16, ~15 min)
- [ ] 🔴 Time the full startup sequence:
  1. Open PowerShell → activate venv → `ollama serve` (if not auto-starting) → `streamlit run app.py`
  2. Target: **under 30 seconds** from cold boot to live UI
- [ ] 🔴 Time the first query: target **under 5 seconds** from pressing Enter to seeing the answer

### 7.3 — Breakage Drills: Intentionally Crash Everything (Day 17, ~45 min)
- [ ] 🔴 **Drill 1: Kill Ollama mid-query.** What error message appears? Add error handling to catch it gracefully.
- [ ] 🔴 **Drill 2: Feed ChromaDB an empty JSON file (`[]`).** Does ingestion crash or handle it? Add a check.
- [ ] 🔴 **Drill 3: Delete the `chroma_db` folder entirely.** Does the app crash on startup or recreate it? It should recreate.
- [ ] 🔴 **Drill 4: Ask a question when ChromaDB has zero documents.** Does it return "no data" or crash?
- [ ] 🔴 **Drill 5: Feed a JSON file where metadata has `null` values.** Does ingestion crash? Add null → empty string cleaning.
- [ ] 🔴 **Drill 6: Ask an extremely long question (500+ words).** Does the model handle it or timeout?
- [ ] 🟡 **Drill 7: Run two Streamlit instances on the same port.** Know how to change the port: `streamlit run app.py --server.port 8502`

### 7.4 — Resource Management (Day 17, ~15 min)
- [ ] 🔴 Check your laptop's RAM usage during a query: Open Task Manager → Performance → Memory
- [ ] 🔴 Know that `llama3.2:3b` uses ~2GB RAM. If your laptop has 8GB total, you have room.
- [ ] 🟡 If RAM is tight, know how to unload a model: `ollama stop llama3.2:3b`
- [ ] 🟡 Know that ChromaDB is disk-based — it barely uses RAM

### ✅ Phase 7 Checkpoint
> Your entire stack runs in Airplane Mode with zero internet. You've intentionally broken every component and know exactly what the error looks like and how to fix it. Nothing can surprise you.

---

## Phase 8: Git, Pitch Prep & War Room (Days 18–19)
*Code is done. Now package it, rehearse, and simulate the real event.*

### 8.1 — Git & GitHub Basics (Day 18, ~30 min)
- [ ] 🔴 Understand what Git is:
  > Git is a save-point system. Like quicksaving in a video game — you can always go back to a previous version if something breaks.
- [ ] 🔴 Learn these 6 Git commands:
  ```powershell
  git init                          # Start tracking this folder
  git add .                         # Stage all changed files
  git commit -m "Added RAG engine"  # Save a checkpoint with a description
  git status                        # Show what's changed since last save
  git log --oneline -5              # Show last 5 save points
  git push                          # Upload to GitHub (backup)
  ```
- [ ] 🔴 Create a GitHub repository and push your code
- [ ] 🟡 Write a professional `README.md` — this is what judges see first on your repo
- [ ] 🟡 Add a `.gitignore` file to exclude `venv/`, `chroma_db/`, `__pycache__/`

### 8.2 — Know Your Architecture Pitch (Day 18, ~30 min)
- [ ] 🔴 Be able to explain the full pipeline in 60 seconds using this structure:
  1. "We ingest raw oilfield PDFs and extract structured text chunks with geological metadata."
  2. "Each chunk is embedded into a 384-dimensional vector and indexed in a local ChromaDB database."
  3. "When a user asks a question, we perform cosine similarity search with metadata filters to retrieve the top 3 relevant excerpts."
  4. "These excerpts are injected into a prompt with strict grounding instructions and sent to a local Llama 3.2 model running entirely offline via Ollama."
  5. "The response includes verifiable citations — well name, page number, and confidence score — so the user can trace every claim back to the source document."
- [ ] 🔴 Be able to answer these judge questions confidently:
  - "What happens if the AI doesn't know the answer?" → "Our similarity threshold detects low-confidence retrievals and the system explicitly states 'data not available' rather than guessing."
  - "Does this need the internet?" → "No. The entire stack — model, database, embeddings, and UI — runs 100% offline in airplane mode."
  - "How do you prevent hallucination?" → "Three layers: similarity threshold filtering, strict system prompt grounding rules, and automated benchmark testing."
  - "What if we give you a CSV instead of PDFs?" → "We have a pre-built LightGBM pipeline and a Text-to-SQL interface ready to deploy in under 10 minutes."

### 8.3 — War Room Simulation (Day 19, ~90 min)
- [ ] 🔴 Run the full dress rehearsal with your teammates:
  1. Cold-start the entire system (pretend it's November 7 morning)
  2. Geologist 1 loads a FRESH PDF that was NOT used during development
  3. You ingest the new data into ChromaDB
  4. All three run 10 questions through the live UI
  5. Geologist 2 runs the benchmark and reads the accuracy score
  6. All three rehearse the 5-minute stage pitch
- [ ] 🔴 Time the full sequence — target: under 15 minutes from cold start to working demo
- [ ] 🔴 Record a 60-second backup demo video (in case the projector fails on stage)

### ✅ Phase 8 Checkpoint
> Your code is on GitHub. You can explain your architecture to a judge in 60 seconds. You've done a full simulation drill with your teammates. You have a backup demo video recorded.

---

## Phase 9: The Final 15% — From "I Coded It" to "I Cannot Shake" (Days 20–21)
*This is the bridge between building the system and being bulletproof under hackathon pressure.*

### 9.1 — Real-World Messy Data Ingestion Drill (Day 20, ~60 min)
- [ ] 🔴 **Create and ingest "Dirty JSON"**:
  - Test missing keys: `{"well_name": null, "content": "..."}` or missing `"chunk_id"`
  - Test unexpected types: `"page_number": "page 4"` instead of `int`, `"porosity": "N/A"`
  - Code defensive defaults in `ingest_worker.py`: `metadata.get("well_name") or "Unknown Well"`
- [ ] 🔴 **Defensive File & Encoding Handling**:
  - Open all files with `open(filepath, 'r', encoding='utf-8', errors='replace')` so strange characters never crash the script
  - Strip unreadable ASCII control characters or messy OCR text artifacts
- [ ] 🔴 **Chunk Size Guards**:
  - Handle extreme chunk sizes: skip chunks with `< 10` characters (empty noise), truncate or split chunks exceeding 512 tokens
- [ ] 🟡 **Deterministic Upsert (Duplicate Prevention)**:
  - If ingestion runs twice on the same document, use `collection.upsert()` with unique IDs (`doc_name_chunk_idx`) instead of `collection.add()` so it never throws duplicate key errors

### 9.2 — The Clean-Slate Rebuild Drill (Muscle Memory) (Day 20, ~45 min)
- [ ] 🔴 **10-Minute ChromaDB Blank Editor Challenge**:
  - Open a blank file `scratch_vector.py`
  - Set a timer for 10 minutes
  - From memory (no notes, no copying): create persistent client, create collection, embed 3 sentences, query top 2, print results
  - If you freeze, check notes, close notes, wipe file, and do it again until it flows naturally
- [ ] 🔴 **10-Minute Ollama Script Challenge**:
  - Open a blank file `scratch_ollama.py`
  - Write a working Ollama query with system prompt, temperature control, and error handling from memory
- [ ] 🔴 **5-Minute Traceback Speedrun**:
  - Deliberately plant 5 errors (missing bracket, typo in dictionary key, wrong port `11435`, wrong method name)
  - Practice locating the exact line number from the traceback and fixing it in under 60 seconds each

### 9.3 — Team Integration & Contract Lock-In (Day 21, ~60 min)
- [ ] 🔴 **The Ingestion Handshake with Geologist 1**:
  - Sit side-by-side with Geologist 1
  - Have them run their PDF extraction on a real oilfield report to generate `extracted_chunks.json`
  - Run your `ingest_worker.py` on their real output file
  - Fix any schema discrepancies (`text` vs `content`, `page` vs `page_number`, `source` vs `doc_name`) and lock the schema
- [ ] 🔴 **The UI Handshake with Geologist 2**:
  - Connect your `query_engine.py` into Geologist 2's Streamlit app
  - Verify every output key: `answer`, `citations`, `confidence_score`
  - Ensure the UI renders confidence badges and citation links cleanly without crashing
- [ ] 🔴 **Cross-Disciplinary Accuracy Review**:
  - Have Geologist 1 ask 5 tough subsurface geology questions (e.g. net pay thickness, water saturation, fault seal)
  - Verify if ChromaDB retrieved the right chunk. Adjust `n_results` (3 vs 5) and similarity thresholds based on geological feedback

### 9.4 — Simulated Chaos & Pressure Drills (Day 21, ~45 min)
- [ ] 🔴 **Chaos Drill 1: The Abrupt Network Drop**:
  - Trigger a query in the UI, then abruptly disconnect Wi-Fi / flip Airplane Mode mid-query
  - Verify local Ollama + ChromaDB completes without hanging
- [ ] 🔴 **Chaos Drill 2: Battery & Thermal Throttling Test**:
  - Unplug the laptop charger and run inference on battery power
  - Measure inference latency. If slow, set Windows Power Mode to "Best Performance"
- [ ] 🔴 **Chaos Drill 3: Deleted Database Recovery Drill**:
  - Delete or rename the `chroma_db` folder
  - Time yourself re-ingesting the raw JSON to a working state (target: under 90 seconds)
- [ ] 🔴 **Chaos Drill 4: Interruption & Distraction Rehearsal**:
  - Have a teammate ask rapid questions or simulate a judge interrupting while you launch the system
  - Keep calm, execute the startup sequence smoothly: `ollama list` → `python ingest_worker.py` → `streamlit run app.py`

### ✅ Phase 9 Checkpoint
> You have ingested messy, dirty real-world data without a single crash. You can write the core ChromaDB and Ollama scripts on a blank screen from memory. You have locked hands with Geologist 1 and Geologist 2 on live files. You have survived chaos drills. You are 100% ready.

---

## The "I Will Not Shake" Confidence Checklist

*On the morning of November 7, before you walk into Eko Hotel, go through this list. Every box should be checked.*

### Technical Confidence
- [ ] I can start the entire system from a cold laptop in under 30 seconds
- [ ] I can ingest a brand-new JSON file into ChromaDB in under 2 minutes
- [ ] I can diagnose whether a bad answer is a retrieval problem, a prompt problem, or a chunking problem
- [ ] I can deploy the LightGBM fallback on an unknown CSV in under 10 minutes
- [ ] I can deploy the Text-to-SQL fallback on a database in under 5 minutes
- [ ] I have tested everything in Airplane Mode and it works

### Debugging Confidence
- [ ] I know what `ConnectionError` means (Ollama isn't running) and how to fix it
- [ ] I know what `KeyError` means (missing dictionary key) and how to fix it
- [ ] I know what `JSONDecodeError` means (AI returned bad format) and how to fix it
- [ ] I know how to read a Python traceback — last line first, then line number
- [ ] I have intentionally broken every component and recovered

### Resilience & Chaos Confidence
- [ ] I can write the core ChromaDB and Ollama code from a blank screen from memory in 10 minutes
- [ ] My ingestion pipeline safely handles null values, missing keys, and dirty character encodings
- [ ] I have tested live handoffs directly with Geologist 1's real output file and Geologist 2's live UI
- [ ] I have tested my system on battery power in Airplane Mode and timed the response latency
- [ ] I can delete the vector database and rebuild it from raw JSON in under 90 seconds

### Team Confidence
- [ ] I know the exact JSON schema Geologist 1 will hand me
- [ ] I know the exact dictionary shape my `query_engine` returns to Geologist 2
- [ ] I have done at least one full simulation drill with both teammates
- [ ] I have rehearsed my architecture pitch at least twice

---

## File Map: What You're Building

```
team_ergon_ai/
├── llm_client.py           ← Day 7:  Python wrapper for Ollama HTTP API
├── schema_enforcer.py      ← Day 8:  Pydantic-powered structured output extraction
├── ai_router.py            ← Day 8:  Local Ollama → Cloud Gemini fallback router
├── vector_store.py         ← Day 9:  ChromaDB vector database wrapper
├── search_service.py       ← Day 10: Filtered vector search + score thresholding
├── ingest_worker.py        ← Day 10: JSON → ChromaDB ingestion pipeline
├── prompt_orchestrator.py  ← Day 11: Context formatting + prompt assembly
├── query_engine.py         ← Day 11: The master RAG orchestrator (your core deliverable)
├── cli_test.py             ← Day 12: Interactive terminal test harness
├── auto_tabular_ml.py      ← Day 14: LightGBM auto-trainer for Scenario B
├── text_to_sql.py          ← Day 15: SQLite Text-to-SQL agent for Scenario B
├── sample_chunks.json      ← Test data for development
├── chroma_db/              ← Auto-created by ChromaDB (local vector database files)
├── venv/                   ← Your Python virtual environment
└── README.md               ← Professional project documentation
```

---

*Last updated: October 15, 2026*
*Team Ergon — NAPE AICE 2026 Hackathon | Eko Hotel & Suites, Lagos | November 7–8*
