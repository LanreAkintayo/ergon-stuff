import os
import json
import chromadb
import pandas as pd
import requests
import ollama
import gradio as gr

# 1. Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="subsurface_cores")

# 2. Load clean cores DataFrame for data viewer tab
csv_path = "data/clean_cores.csv"
df_cores = pd.read_csv(csv_path) if os.path.exists(csv_path) else pd.DataFrame()

# 3. Chief Geologist System Prompt
SYSTEM_PROMPT = """You are a Chief Subsurface Geoscientist assisting an exploration team at the NAPE AICE hackathon.
Your duty is to answer technical questions using ONLY the provided subsurface archive excerpts.

CRITICAL RULES:
1. Base your answer strictly on the provided excerpts.
2. Cite the excerpt(s) you used to support each technical claim (e.g., "[EXCERPT 1]").
3. If the data is absent or insufficient to answer the question, state: 'Data not available in indexed well archives.'
4. Do NOT speculate, extrapolate, or invent reservoir properties under any circumstance.
5. Be concise, professional, and authoritative.
"""

def format_retrieved_context(documents: list[str], metadatas: list[dict]) -> str:
    """Formats raw ChromaDB chunks into numbered excerpts."""
    if not documents:
        return "No relevant subsurface records found."
    excerpts = []
    for i, (doc, meta) in enumerate(zip(documents, metadatas), start=1):
        header = f"[EXCERPT {i} | Well: {meta.get('well_name')} | Field: {meta.get('field', 'N/A')} | Depth: {meta.get('top_depth_m')} - {meta.get('bottom_depth_m')}m]"
        excerpts.append(f"{header}\n\n{doc}")
    return "\n\n".join(excerpts)

def ask_llm(user_prompt: str, system_prompt: str) -> str:
    """Calls Gemini or OpenAI if keys are present; falls back to local Ollama."""
    # 1. Google Gemini
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}"
            payload = {
                "contents": [{"parts": [{"text": user_prompt}]}],
                "systemInstruction": {"parts": [{"text": system_prompt}]}
            }
            res = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=30)
            if res.status_code == 200:
                return res.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
        except Exception:
            pass

    # 2. OpenAI
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        try:
            url = "https://api.openai.com/v1/chat/completions"
            headers = {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"}
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.0
            }
            res = requests.post(url, json=payload, headers=headers, timeout=30)
            if res.status_code == 200:
                return res.json()["choices"][0]["message"]["content"].strip()
        except Exception:
            pass

    # 3. Local Ollama fallback
    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        response = ollama.chat(model="llama3.2:3b", messages=messages, options={"temperature": 0.0})
        return response["message"]["content"]
    except Exception as e:
        return f"Error contacting local AI model: {e}"

def ask_subsurface_ai(user_question: str, top_k: int = 2) -> str:
    """Takes user question -> queries ChromaDB -> formats context -> generates answer."""
    results = collection.query(query_texts=[user_question], n_results=top_k)
    context_block = format_retrieved_context(results["documents"][0], results["metadatas"][0])
    
    user_prompt = f"""--- SUBSURFACE ARCHIVE EXCERPTS ---
{context_block}
----------------------------------

QUESTION: {user_question}

Provide a concise, grounded technical answer citing your sources:"""

    return ask_llm(user_prompt=user_prompt, system_prompt=SYSTEM_PROMPT)

def geologist_chat(message, history):
    """Callback for Gradio ChatInterface."""
    return ask_subsurface_ai(message)

# Build clean Gradio interface
with gr.Blocks(title="Ergon Chief Geoscientist AI") as demo:
    gr.Markdown("# 🛢️ Ergon Chief Geoscientist AI")
    gr.Markdown("Ask technical questions about well cores, formations, depth intervals, and recovery percentages.")
    
    with gr.Tab("💬 Geologist Chat"):
        gr.ChatInterface(
            fn=geologist_chat,
            examples=[
                "Which cores had recovery of at least 90%, and at what depths?",
                "What core was recovered from the Middle Agbada formation and what was its recovery?",
                "Show all core retrieval details for Well-Alpha."
            ]
        )
        
    with gr.Tab("📋 Indexed Cores Archive"):
        gr.Markdown("### Ground Truth Tabular Records")
        gr.DataFrame(df_cores)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
