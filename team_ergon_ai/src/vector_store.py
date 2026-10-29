import chromadb.utils.embedding_functions as ef
import chromadb
import numpy as np 
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "chroma_db")

class SubsurfaceVectorStore:
    def __init__(self, persist_dir: str = DB_DIR, collection_name: str = "subsurface_docs"):
        # Initialize the persistent client pointing to persist_dir
        self.client = chromadb.PersistentClient(path=persist_dir)
        
        # Create or get the collection
        self.collection = self.client.get_or_create_collection(name=collection_name)
        
        
    def count(self) -> int:
        return self.collection.count()
    
    def reset(self):
        """Wipes the collection clean so we can re-ingest fresh data"""
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(self.collection.name)
        print(f"[+] Collection `{self.collection.name}` reset to clean slate")
    
    def add_chunks(self, chunks: list[dict]):
        # Prepare list of ids, texts and metadatas
        ids = []
        texts = []
        metadatas = []
        
        for each_chunk in chunks:
            ids.append(each_chunk["chunk_id"])
            texts.append(each_chunk["text"])
            
            meta = each_chunk.get("metadata") or {
                k: v for k, v in each_chunk.items() if k not in ["chunk_id", "text"]
            }
            metadatas.append(meta)
            
        self.collection.upsert(
            ids=ids,
            documents=texts,
            metadatas=metadatas
        )
        
        print(f"[+] Added {len(chunks)} chunks to the vector store.")
    
    def query(self, text: str, n_results: int = 3, where: dict = None):
        """Query the vector store with optional metadata filtering"""
        kwargs = {
            "query_texts": [text],
            "n_results": n_results
        }
        if where:
            kwargs["where"] = where
            
        return self.collection.query(**kwargs)
    
    

if __name__ == "__main__":
    store = SubsurfaceVectorStore()
    
    sample_chunks = [
        {
            "chunk_id": "chk_01",
            "text": "Well Bonga-01 encountered clean reservoir sand at 9100 ft with 22% porosity.",
            "metadata": {"well": "Bonga-01", "depth": 9100.0}
        },
        {
            "chunk_id": "chk_02",
            "text": "Well Bonga-03 penetrated high pay zone with significant oil shows at 9350 ft.",
            "metadata": {"well": "Bonga-03", "depth": 9350.0}
        },
        {
            "chunk_id": "chk_03",
            "text": "The drilling crew took a safety break at the base camp in Lagos.",
            "metadata": {"well": "BaseCamp", "depth": 0.0}
        }
    ]
    
    store.add_chunks(sample_chunks)
    # print("Total chunks in the database: ", store.count())
    
    print(store.query(text="What is the porosity of well Bonga-01?", n_results=3))
    # print(store.query(text="oil show depth", n_results=2, where={"well": "Bonga-03"}))
    
# def cosine_similarity(v1, v2):
#     # Dot product divided by the magnitudes (lengths) of both vectors
#     return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    

# # ChromaDB comes with a free, fast, local embedding model
# embed_fn = ef.DefaultEmbeddingFunction()

# # Let's convert 3 sentences into numbers:
# vectors = embed_fn([
#     "High porosity sandstone reservoir",
#     "Rock with 28% pore volume and good storage capacity",
#     "The sky is blue today in Lagos"
# ])


# sim_1_and_2 = cosine_similarity(vectors[0], vectors[1])
# sim_1_and_3 = cosine_similarity(vectors[0], vectors[2])

# print(f"\nSimilarity between Reservoir and Rock: {sim_1_and_2:.4f}")
# print(f"Similarity between Reservoir and Sky:  {sim_1_and_3:.4f}")


# # print("Number of dimensions in vector 1:", len(vectors[0]))
# # print("First 5 coordinates of vector 1:", vectors[0][:5])


