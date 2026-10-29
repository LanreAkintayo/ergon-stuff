from ai_router import AIRouter
from prompt_orchestrator import format_context_block, build_rag_prompt
from search_service import search_with_filters


class SubsurfaceQueryEngine:
    def __init__(self):
        self.router = AIRouter()
        

    def ask(self, question: str, well_filter: str = None) -> dict:
        chunks = search_with_filters(question, well_name=well_filter)
        
        # If no chunks survived the firewall, don't even waste time calling the LLM!
        if not chunks:
            return {
                "answer": "Data not available in indexed well archives.",
                "citations": []
            }
        
        formatted_context = format_context_block(chunks)
        system_prompt, user_prompt = build_rag_prompt(question, formatted_context)
        
        response = self.router.generate(user_prompt, system=system_prompt)

        # Package citations for Geologist 2's Streamlit badges:
        citations = []
        for c in chunks:
            meta = c.get("metadata", {})
            citations.append({
                "chunk_id": c.get("chunk_id"),
                "well": meta.get("well") or meta.get("well_name") or "Unknown",
                "depth": meta.get("depth") or meta.get("depth_ft"),
                "score": int(c.get("similarity", 0) * 100),
                "excerpt": c.get("text")
            })
        
        # If the LLM realized the retrieved text doesn't contain the answer,
        # don't attach irrelevant citations to the UI:
        if "Data not available" in response:
            citations = []  
        

        return {
            "answer": response,
            "citations": citations
        }


if __name__ == "__main__":
    engine = SubsurfaceQueryEngine()
    
    print("\n--- TEST 1: Real Subsurface Query ---")
    res1 = engine.ask("What is the porosity of Bonga-01?")
    print("AI Answer:\n", res1["answer"])
    print("\nCitations:")
    for cit in res1["citations"]:
        print(f"  • {cit['well']} (Depth: {cit['depth']} ft, Confidence: {cit['score']}%)")

    print("\n--- TEST 2: Irrelevant / Missing Well Query ---")
    res2 = engine.ask("What is the porosity of Well Chevron-99?")
    print("AI Answer:\n", res2["answer"])
    print("Citations Count:", len(res2["citations"]))
    
    print("\n--- TEST 3: Query with Well Filter (Bonga-03) ---")
    res3 = engine.ask("What oil shows were found?", well_filter="Bonga-03")
    print("AI Answer:\n", res3["answer"])
    print("\nCitations:")
    for cit in res3["citations"]:
        print(f"  • {cit['well']} (Depth: {cit['depth']} ft, Confidence: {cit['score']}%)")
