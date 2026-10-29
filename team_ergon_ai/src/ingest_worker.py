import os
import json
from vector_store import SubsurfaceVectorStore

def run_ingestion(json_filename: str = "clean_chunks.json"):
    # 1. Resolve exact file path (avoids FileNotFoundError)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, json_filename)
    
    # Check data/ subdirectory if not in root
    if not os.path.exists(file_path):
        data_path = os.path.join(base_dir, "data", json_filename)
        if os.path.exists(data_path):
            file_path = data_path
        else:
            print(f"[!] Error: {file_path} not found!")
            return 0
        
    print(f"[*] Reading geology chunks from: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)
        
    print(f"[*] Loaded {len(chunks)} chunks from disk.")
    
    # 2. Connect to vector store
    store = SubsurfaceVectorStore()
    
    # 3. Clean slate reset (wipes old drafts)
    store.reset()
    
    # 4. Ingest new chunks
    store.add_chunks(chunks)
    
    # 5. Verify total count
    total = store.count()
    print(f"✅ Ingestion complete! Total active chunks in ChromaDB: {total}")
    return total

if __name__ == "__main__":
    run_ingestion()
