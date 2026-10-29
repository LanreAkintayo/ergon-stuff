# Team Ergon: The Master Playbook
## NAPE AICE 2026 Hackathon | "Unlocking Dormant Value"
### Eko Hotel & Suites, Lagos | November 7–8, 2026

---

> [!IMPORTANT]
> This document is for the entire team. Read it together if you can. You each have individual preparation curricula. This document is different. This is the document that shows HOW your skills connect like puzzle pieces, and WHAT the exact play is for every possible challenge NAPE throws at you on November 7.
>
> Read this before you start your individual curricula. Refer back to it every week.

---

## Part 1: The Formation

| What The Judges Need | Who Provides It |
| :--- | :--- |
| Deep domain understanding of Niger Delta reservoirs, formations, and well operations | **Geologist 1 & Geologist 2** |
| A working AI system that runs offline without cloud dependency | **Computer Scientist (CS 1)** |
| Data that makes geological sense when fed into the AI | **Geologist 1** (smart chunking) |
| A system prompt that talks like a Chief Geoscientist | **Geologist 2** (prompt architecture) |
| A backend that retrieves the right pages in milliseconds | **CS 1** (ChromaDB + RAG engine) |
| Quantified proof that the AI is accurate, not hallucinating | **Geologist 2** (benchmark evaluation) |
| A beautiful, intuitive dashboard that executives can use | **Geologist 2** (Streamlit UI) |
| Business case showing millions saved in operational efficiency | **All Three** (joint pitch) |

---

## Part 2: The Universal Pipeline (How You Are All Connected)

This is the single most important diagram in this document. 
Every line of code, every chunk of text, and every test question you work on individually flows through this unified pipeline:

```text
╔══════════════════════════════════════════════════════════════════════════╗
║                   TEAM ERGON UNIFIED PIPELINE                           ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  [ANY NAPE DATA FORMAT]                                                  ║
║   PDFs, Scanned Reports, LAS Files, CSVs, Excel Sheets                  ║
║         │                                                                ║
║         ▼                                                                ║
║  ┌──────────────────────────────┐                                        ║
║  │  GEOLOGIST 1: Data Ingestor  │  ← Your individual curriculum         ║
║  │                              │                                        ║
║  │  • Extracts text from PDFs   │                                        ║
║  │  • OCR for scanned reports   │                                        ║
║  │  • Reads .LAS wireline logs  │                                        ║
║  │  • Cleans -999.25 nulls      │                                        ║
║  │  • Domain-aware chunking     │                                        ║
║  │  • Tags every chunk with     │                                        ║
║  │    well_name, depth, page    │                                        ║
║  │                              │                                        ║
║  │  OUTPUT: well_chunks.json    │                                        ║
║  └─────────────┬────────────────┘                                        ║
║                │ hands off JSON file                                     ║
║                ▼                                                         ║
║  ┌──────────────────────────────┐     ┌─────────────────────────────┐   ║
║  │  CS 1: Backend Engine     │     │  GEOLOGIST 2: Intelligence   │   ║
║  │                              │ ◄───│  Layer                       │   ║
║  │  • Generates text embeddings │     │                              │   ║
║  │  • Indexes chunks into       │     │  • Writes system prompts     │   ║
║  │    ChromaDB vector store     │     │  • Anti-hallucination rules  │   ║
║  │  • Runs similarity search    │     │  • Domain query expander     │   ║
║  │  • Filters by well/depth     │     │  • Golden 10 test benchmark  │   ║
║  │  • Injects context into      │     │  • Streamlit dashboard       │   ║
║  │    LLM prompt template       │     │  • Citation badge renderer   │   ║
║  │  • Calls local Ollama model  │     │  • Executive report button   │   ║
║  │  • Streams answer back       │     │                              │   ║
║  │                              │     │  OUTPUT: app.py + prompts    │   ║
║  │  OUTPUT: query_engine()      │     └─────────────────────────────┘   ║
║  └─────────────┬────────────────┘                                        ║
║                │                                                         ║
║                ▼                                                         ║
║  ┌──────────────────────────────────────────────────────────┐            ║
║  │  FINAL PRODUCT: Subsurface Intelligence Web App          │            ║
║  │                                                          │            ║
║  │  A judge types: "What is the porosity of Sand B?"       │            ║
║  │  ↓ Domain query expander enriches keywords              │            ║
║  │  ↓ ChromaDB fetches top 4 relevant well report chunks   │            ║
║  │  ↓ Similarity threshold drops any weak matches          │            ║
║  │  ↓ Context injected into Chief Geologist system prompt  │            ║
║  │  ↓ Local Ollama model generates grounded answer          │            ║
║  │  ↓ Citation cards show: Well, Page, Confidence Score    │            ║
║  │  Result: Professional, verified, real-time answer       │            ║
║  └──────────────────────────────────────────────────────────┘            ║
╚══════════════════════════════════════════════════════════════════════════╝
```

> [!TIP]
> **Print this pipeline and stick it somewhere everyone can see during the hackathon weekend.** When someone gets confused about what to do next, point to the diagram. Every task maps to a box in this chart.

---

## Part 3: The 4 Scenario Playbooks (No Matter What NAPE Gives You)

This is the heart of the playbook. On the morning of November 7, NAPE will announce the challenge. Within 10 minutes, Team Ergon must identify the scenario type and activate the matching play. There are only 4 possible scenarios.

---

### 📋 Scenario A: "We Give You Documents" (PDFs, Reports, Scanned Files)
*This is the highest-probability scenario given the theme "Unlocking Dormant Value" and the DeployEdu curriculum NAPE assigned.*

**Examples of Scenario A challenges:**
- "Here are 30 historical well completion reports. Build a system to search and extract insights."
- "Analyze these legacy field development plans and identify dormant assets."
- "Help engineers query these archived drilling reports without reading every page."

**Who does what:**

| Time | CS 1 | Geologist 1 | Geologist 2 |
| :--- | :--- | :--- | :--- |
| **Hour 0–1** | Pull chromaDB and Ollama. Confirm local model is alive. Test `query_engine.py` with dummy data. | Download and inspect the PDF files. Skim each one: How many pages? Digital or scanned? Tables or pure text? | Open Google AI Studio. Start drafting the system prompt using the team's baseline template. |
| **Hour 1–3** | Stand by for Geologist 1's hand-off. Prepare ingestion worker. | Run `extract_full_pdf()` on all files. Apply OCR if pages are scanned. Chunk the documents. Export `chunks.json`. | Finalize system prompt and guardrails. Write the first 5 "Golden" test questions based on the actual document content. |
| **Hour 3–5** | Ingest `chunks.json` into ChromaDB. Run first vector search queries in terminal. Report retrieval quality to team. | Validate JSON quality with `validate_chunks()`. Fix any noise, garbled text, or wrong metadata. | Wire up the Streamlit UI. Test the chat interface against the backend. |
| **Hour 5–8** | Performance tuning: adjust `top_k`, similarity threshold. Ensure sub-second query latency. | Stress-test the system: type all 10 Golden benchmark questions into the app. Flag any wrong answers. | Run the automated evaluation benchmark script. Record the final accuracy score for the pitch slide. |
| **Hour 8–12** | Code freeze. Backup all files to USB and GitHub. | Prepare domain-specific talking points for the stage pitch. | Polish UI, record demo video backup, finalize slides. |

**The Team Ergon Advantage in Scenario A:**
- Geologist 1 can identify which pages have stratigraphy tables and which are just company letterhead — a computer scientist cannot.
- Geologist 2 can write the system prompt using real formation names like "Agbada", "Akata", and "Benin" — making the AI sound authoritative.
- CS 1 ensures the database never crashes and retrieval stays fast — the geologists don't have to worry about any of that.

---

### 📊 Scenario B: "We Give You Numbers" (CSVs, Excel, Well Log Data)
*High probability based on previous NAPE challenges: Lithology prediction, separator composition, seismic facies.*

**Examples of Scenario B challenges:**
- "Build a model to predict lithology (rock type) from well log readings."
- "Predict composition of separator output from pressure, temperature, and GOR."
- "Classify seismic facies from amplitude and frequency attributes."

**Who does what:**

| Time | CS 1 | Geologist 1 | Geologist 2 |
| :--- | :--- | :--- | :--- |
| **Hour 0–1** | Open `auto_tabular_ml.py`. Load the CSV. Check shape, column names, and data types. | Inspect the column headers immediately: identify which columns are features (inputs) and which is the prediction target. Flag any columns that are physically impossible (e.g., negative porosity). | Begin writing a brief domain explanation of what the target variable means physically (e.g., "Lithology: 0=Shale, 1=Sandstone, 2=Limestone"). |
| **Hour 1–2** | Apply null cleaning: replace -999.25 with NaN. Let Geologist 1 guide which columns need petrophysical cleaning. | Clean oilfield-specific bad values. Compute derived columns: Vshale from Gamma Ray, acoustic impedance from Density × Sonic, N/G ratio. | Start the Streamlit UI shell: input sidebar with column selectors and a results table display. |
| **Hour 2–4** | Train LightGBM on cleaned data. Print feature importance chart. Iterate with Geologist 1 to add more engineered features. | Validate predictions physically: "The model says this 150-ft interval is all shale, but the GR is 45 API — that's definitely sand. Something is wrong." | Design the output visualization: a depth-track log plot showing actual vs. predicted lithology. |
| **Hour 4–6** | Wrap the model in a Streamlit UI: CSV upload button → predictions table → downloadable results CSV. | Test model outputs against domain knowledge. Write 3 bullet points explaining why each engineered feature improves the model. | Finalize the pitch narrative: quantify how long manual lithology picking takes vs. automated AI prediction. |

**Text-to-SQL variation of Scenario B:**
If NAPE gives you a relational production database instead of raw CSV files:
- CS 1 deploys `text_to_sql.py` with SQLite in under 10 minutes.
- Geologist 2 writes 5 natural-language queries to test the interface.
- Geologist 1 validates that the SQL results make physical sense.

---

### 🔀 Scenario C: "Hybrid" (Some Documents + Some Tables)
*Possible: NAPE gives you a mix of PDF field reports AND well log CSVs.*

**Example:** "Here are 20 historical completion reports and 5 well log datasets. Build a tool that integrates both."

**The play:**
1. CS 1 splits the team immediately: "Geologist 1 handles the PDFs, I handle the CSVs."
2. Both pipelines run in parallel:
   - Geologist 1 produces `pdf_chunks.json`
   - CS 1 loads CSVs into a LAS/pandas pipeline and generates summary text (e.g., "Well-01 interval 9200–9450 ft: avg porosity 22.3%, avg GR 42 API.")
3. CS 1 merges both text sources into one ChromaDB collection.
4. Geologist 2's UI adds a "Data Source" filter: PDF Archive vs. Well Log Curves.
5. The AI can now answer questions that span both sources — an impossibly hard task for any team that didn't prepare this formation.

---

### ❓ Scenario D: "The Curveball" (Something We Haven't Seen Before)
*What if NAPE gives us something completely different?*

**Examples:**
- "Build an AI that monitors pipeline anomalies from sensor data streams."
- "Analyze social media and news for oil price sentiment."
- "Translate legacy FORTRAN seismic processing code using AI."

**The Anti-Panic Protocol (Non-negotiable team rule):**

When the challenge is announced and it's not A, B, or C — do the following:
1. **Do not react for 5 minutes.** Read the problem statement three times.
2. The entire team answers this question together: *"What is the fundamental data format? Text, numbers, or both?"*
3. Whatever it is, your pipeline handles it. Text → RAG. Numbers → LightGBM or SQL.
4. Ask: *"What does the user need to DO with our system?"* Search? Predict? Classify? Visualize?
5. Geologist 2 writes the system prompt defining what role the AI plays in this new context.
6. Geologist 1 ingests and cleans whatever data format was given.
7. CS 1 runs the backend engine — the core code does not change.

> [!WARNING]
> **The #1 mistake teams make in Scenario D: Trying to build something completely new from scratch.**
> You do NOT rebuild from scratch. You change what flows INTO your pipeline. The pipeline itself is unchanged.
> Scenario D is won by the team that stays calm, reuses their foundation, and adapts faster than everyone else.

---

## Part 4: The 3 Team Integration Sessions (Do These Together)

Individual study is necessary. But the following 3 sessions must be done together as a team — not individually, not asynchronously. Schedule them now.

### Session 1: The Data Contract Meeting (Week 1, Day 5–7)
**Purpose:** Agree on the exact JSON format that connects Geologist 1's output to the CS 1's input.

**What happens:**
- CS 1 explains: "I need a list of dictionaries. Each dictionary must have a `text` key and a `metadata` key."
- Geologist 1 asks: "What fields do you need inside metadata?"
- CS 1 answers: "At minimum: `well_name`, `page_number`. Optionally: `depth_mentioned`, `section`, `formation`."
- Geologist 2 adds: "I also need `page_number` in every chunk so I can render citation badges in the UI."
- **Outcome:** Everyone writes down and agrees on this shared schema:

```json
{
    "text": "The Agbada Formation sandstone at 9,200 ft shows 24% porosity.",
    "metadata": {
        "well_name": "OML-42 Well-01",
        "page_number": 14,
        "section": "Reservoir Description",
        "depth_mentioned": 9200,
        "formation": "Agbada"
    }
}
```

This schema is your team's **API contract**. Geologist 1 produces it. CS 1 consumes it. Geologist 2 displays it. If this schema is agreed on in Week 1, there will be zero integration bugs in Week 3.

---

### Session 2: The Red-Team Jam Session (Week 2, Day 11–13)
**Purpose:** Break the AI together before the judges do.

**What happens:**
- CS 1 has the app running locally.
- All three sit around one screen.
- Geologist 1 fires hard geological questions designed to trip the system up:
  - *"What is the GOR in Well-04?"* (if Well-04 doesn't exist in your data)
  - *"Compare the porosity of Sand B in Well-01 vs Well-02."* (a multi-well comparison query)
  - *"What caused the kick on November 14th?"* (a date-specific query with no date metadata)
- When the AI fails or hallucinates, the team diagnoses together:
  - Is it a **retrieval failure**? (CS 1 adjusts `top_k` or similarity threshold)
  - Is it a **prompt failure**? (Geologist 2 adds a new guardrail)
  - Is it a **chunking failure**? (Geologist 1 refines chunk boundaries or metadata)
- Run through at least 20 questions in one session.

This session is where your individual skills multiply. One person cannot red-team their own system effectively.

---

### Session 3: The War Room (Week 3, Day 19–21)
**Purpose:** Full dress rehearsal. Simulate the entire hackathon in 2 hours.

**What happens:**
1. CS 1 starts the local Ollama server and Streamlit app cold (as if it's November 7 morning).
2. Geologist 1 loads a fresh PDF (one that was not used during development) and runs the full ingestion pipeline.
3. CS 1 ingests the new data into ChromaDB.
4. All three run 10 questions through the live UI.
5. Geologist 2 runs the automated benchmark and reads out the accuracy score.
6. All three rehearse the full 5-minute stage pitch — CS 1 presents the architecture slide, Geologist 1 presents the data pipeline slide, Geologist 2 demonstrates the live UI and reads the benchmark scorecard.

**If you can run the War Room cleanly, you are ready for November 7.**

---

## Part 5: Hackathon Day Hour-by-Hour Execution Plan

The challenge is announced at the event. Here is your exact game plan:

| Time | Team Action |
| :--- | :--- |
| **8:00 AM — Arrival** | Set up at your assigned workstation. CS 1 boots Ollama and confirms it is running. All three read the challenge brief together in silence for 5 minutes. |
| **8:15 AM — Scenario Identification** | As a team, answer: "Text, Numbers, or Both?" Lock in Scenario A, B, or C within 15 minutes. Do NOT debate for longer than this. |
| **8:30 AM — Work Begins** | Each team member opens their laptop and activates their assigned role per the Scenario Playbook. The clock is running. |
| **10:30 AM — First Sync** | 10-minute standup. CS 1: "Backend status?" Geologist 1: "How many chunks ingested?" Geologist 2: "Is the prompt ready?" |
| **12:00 PM — Working Baseline** | By midday, the app must be running end-to-end, even imperfectly. A basic working demo beats a perfect unfinished one every single time. |
| **1:00 PM — Lunch Break (Enforced)** | Mandatory 30-minute break. No laptops. Tired brains make bad decisions. |
| **2:00 PM — Quality & Polish** | Fix the bugs that matter. Geologist 2 runs benchmark. CS 1 fixes low similarity scores. Geologist 1 re-chunks any problem sections. |
| **5:00 PM — Code Freeze** | Stop adding features. Whatever is in the app at 5 PM is what you present. Freeze the codebase. |
| **5:00 PM – 7:00 PM — Pitch Prep** | All three rehearse the stage pitch at least twice. Record the backup demo video. Charge all laptops. |
| **7:00 PM onwards** | Rest, sleep, eat properly. A rested team performs 50% better on stage than an exhausted one. |

---

## Part 6: Team Defense Protocols (Team Rules)

These rules are non-negotiable. Discuss them openly as a team before November 7.

#### Rule 1: The 2-Hour Lock-In Rule
Within 2 hours of the challenge announcement, the team must lock in one scenario and one approach. No pivoting after 2 hours, no matter what another team is doing or what someone saw on Twitter.

#### Rule 2: The 5 PM Code Freeze Rule
At 5:00 PM on November 7, no new features are added. Bugs that exist at 5 PM will be fixed. New ideas will be written in a notebook for after the hackathon. A working product beats a half-finished ambitious one every time.

#### Rule 3: The 60-Second Video Rule
By 5:00 PM, Geologist 2 must have a recorded screen video of the working app. If anything fails on stage — projector, laptop, internet — you smile calmly, open the video on your phone, and narrate it live. Judges care about the idea and the solution, not about live demo glitches.

---

## 3-Week Shared Team Calendar

| Day | CS 1 Focus | Geologist 1 Focus | Geologist 2 Focus | Team Together |
| :--- | :--- | :--- | :--- | :--- |
| 1–2 | Ollama install & Python client | Python strings, lists, dicts | Google AI Studio + Prompt Basics | — |
| 3–4 | Pydantic JSON schemas | Python conditions & pandas CSV | Negative constraints & guardrails | — |
| 5–6 | Cloud fallback router & embeddings | Python functions | Temperature = 0 & query expander | **Data Contract Session** |
| 7 | ChromaDB setup milestone | Week 1 mini-project | Golden 10 test suite | — |
| 8–9 | Ingestion worker | pdfplumber text extraction | RAG eval science | — |
| 10–11 | Metadata filtering & retrieval | Table extraction & combining | Streamlit basics (metrics + chat) | — |
| 12–13 | RAG orchestrator core | Domain-aware chunking | Streamlit sidebar filters | **Red-Team Jam Session** |
| 14 | CLI end-to-end test | Week 2 milestone | Week 2 milestone | — |
| 15–16 | Streamlit integration | Depth extraction & full tagger | Citation badges & source preview | — |
| 17–18 | Offline airplane mode test | Multi-PDF batch processing | Executive report generator | — |
| 19 | Scenario B LightGBM template | Quality validation script | Stage curveball protocols | **War Room Rehearsal** |
| 20 | Scenario B Text-to-SQL template | Day 20 simulation drill | Record 60-sec demo video | — |
| 21 | GitHub repo & README | Hackathon simulation drill | Full integration test | **Full Dress Rehearsal** |
| Nov 5–6 | Full system test. Code freeze prep. No new features. Rest. | — | — | — |
| **Nov 7** | **NAPE AICE 2026 Hackathon — Eko Hotel & Suites, Lagos** |

---

*Team Ergon — Computer Scientist + Geologist 1 + Geologist 2*
*NAPE AICE 2026 Hackathon | Eko Hotel & Suites, Lagos | November 7–8, 2026*
*Theme: "Unlocking Dormant Value"*
