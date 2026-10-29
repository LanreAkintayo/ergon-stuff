import json
from pydantic import BaseModel, ValidationError

class OilFieldChunk(BaseModel):
    chunk_id: str
    well_name: str
    porosity: float
    text: str
    
    
# Let's create raw_chunks.json
raw_dataset = [
    {"chunk_id": "c1", "well_name": "Bonga-01", "porosity": 0.22, "text": "Clean sand at 9100 ft."},
    {"chunk_id": "c2", "well_name": "Bonga-02", "porosity": "CORRUPT_VALUE", "text": "Shale barrier."}, # ❌ Bad porosity!
    {"chunk_id": "c3", "well_name": "Bonga-03", "porosity": 0.28, "text": "High pay zone with oil shows."},
    {"chunk_id": "c4", "well_name": "Bonga-04", "porosity": 0.19, "text": "Deep channel sand."}
]

with open("raw_chunks.json", "w", encoding="utf-8") as f:
    json.dump(raw_dataset, f, indent=4)


# Let's read it back
with open(f.name, "r", encoding="utf-8") as r_f:
    raw_chunks = json.load(r_f)

clean_chunks = []
for raw_chunk in raw_chunks:
    try:
        field_chunk = OilFieldChunk(**raw_chunk)
        clean_chunks.append(field_chunk.model_dump())
    except ValidationError as e:
        print(f"[!] SKIPPED: Chunk `{raw_chunk.get("chunk_id")}` is corrupt and was rejected")
        

with open("clean_chunks.json", "w", encoding="utf-8") as n_f:
    json.dump(clean_chunks, n_f, indent=4)      
    
print(f"[+] Ingestion complete! Saved {len(clean_chunks)} clean chunks to {n_f.name}")
  