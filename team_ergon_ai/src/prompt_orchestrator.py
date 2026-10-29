def format_context_block(chunks: list[dict]) -> str:
    """Takes retrieved chunks and formats them as numbered excerpts with metadata headers"""
    if not chunks:
        return "No relevant subsurface records found."

    formatted_excerpts = []

    for i, chunk in enumerate(chunks, start=1):
        meta = chunk.get("metadata", {})
        well = meta.get("well") or meta.get("well_name") or "Unknown Well"
        depth = meta.get("depth") or meta.get("depth_ft")

        # Format relevance percentage (e.g., 0.6953 -> 70%)
        relevance = int(chunk.get("similarity", 0) * 100)

        depth_info = f" | Depth: {depth} ft" if depth else ""
        header = f"[EXCERPT {i} | Well: {well}{depth_info} | Relevance: {relevance}%]"

        text = chunk.get("text", "").strip()
        formatted_excerpts.append(f"{header}\n{text}")

    return "\n\n".join(formatted_excerpts)


RAG_SYSTEM_PROMPT = """You are a Chief Subsurface Geoscientist assisting an exploration team at the NAPE AICE hackathon.
Your duty is to answer technical questions using ONLY the provided subsurface archive excerpts.

CRITICAL RULES:
1. Base your answer strictly on the provided excerpts.
2. Cite the excerpt(s) you used to support each technical claim (e.g., "[EXCERPT 1]").
3. If the data is absent or insufficient to answer the question, state: 'Data not available in indexed well archives.'
4. Do NOT speculate, extrapolate, or invent reservoir properties under any circumstance.
5. Be concise, professional, and authoritative.
"""


def build_rag_prompt(question: str, context_block: str) -> tuple[str, str]:
    """Combines user question and formatted excerpts into (system_prompt, user_prompt)"""

    user_prompt = f"""--- SUBSURFACE ARCHIVE EXCERPTS ---
{context_block}
----------------------------------

QUESTION: {question}

Provide a concise, grounded technical answer citing your sources:"""

    return RAG_SYSTEM_PROMPT, user_prompt


if __name__ == "__main__":
    sample_chunks = [
        {
            "chunk_id": "chk_01",
            "text": "Well Bonga-01 encountered clean reservoir sand at 9100 ft with 22% porosity.",
            "metadata": {"well": "Bonga-01", "depth": 9100.0},
            "similarity": 0.6953,
        },
        {
            "chunk_id": "chk_02",
            "text": "Bonga-03 penetrated high pay zone with oil shows at 9350 ft.",
            "metadata": {"well": "Bonga-03", "depth": 9350.0},
            "similarity": 0.5512,
        },
    ]

    context = format_context_block(sample_chunks)
    system_prompt, user_prompt = build_rag_prompt(
        "What is the porosity of Bonga-01?", context
    )

    print("--- ASSEMBLED USER PROMPT ---")
    print(user_prompt)
