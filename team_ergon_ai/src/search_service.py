from vector_store import SubsurfaceVectorStore


def search_with_filters(query_text: str, well_name: str = None, min_similarity: float = 0.45):
    # Query the vector store
    vector_store = SubsurfaceVectorStore()
    filter = {"well_name": well_name} if well_name else None
    query_result = vector_store.query(text=query_text, where=filter)
    
    
    
    ids = query_result["ids"][0]
    distances = query_result["distances"][0]
    documents = query_result["documents"][0]
    metadatas = query_result["metadatas"][0]
    
    verified_chunks = []
    
    # Conver the distance to similarity: Similarity  = 1 - distance
    for chunk_id, distance, text, metadata in zip(ids, distances, documents, metadatas):
        similarity = 1.0 - (distance / 2.0)
        print(f"Distance: {distance}", f"Similarity: {similarity}", f"Min Similarity: {min_similarity}")
        
        if similarity >= min_similarity:
            verified_chunks.append({
                "chunk_id": chunk_id,
                "text": text,
                "metadata": metadata,
                "similarity": round(similarity, 4)
            })
    
    return verified_chunks


if __name__ == "__main__":
    print("\n--- Test 1: Good Query (Should find Bonga-01) ---")
    results = search_with_filters("What is the porosity of Bonga-01")
    print(f"Found {len(results)} relevant chunks:")
    for r in results:
        print(r)

    print("\n--- Test 2: Irrelevant Query (Firewall should block it!) ---")
    results = search_with_filters("What is the price of yam in Lagos market?")
    print(f"Found {len(results)} relevant chunks (Expect 0):", results)
