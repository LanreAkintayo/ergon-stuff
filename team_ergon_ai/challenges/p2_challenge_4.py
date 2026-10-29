from pydantic import BaseModel, ValidationError


class WellRecord(BaseModel):
    well_id: str
    depth_ft: int
    porosity: float
    is_active: bool = True
    
    
good_data = {
    "well_id": "OML-130-01",
    "depth_ft": 9800,
    "porosity": 0.24
}

record = WellRecord(**good_data)
print(record.well_id)
print(record.porosity)
print(record.is_active)

bad_data = {
    "well_id": "OML-130-02",
    "depth_ft": "NOT_A_DEPTH",   # ❌ String instead of integer
    "porosity": "HIGH_POROSITY"   # ❌ String instead of float!
}

try:
    corrupt_record = WellRecord(**bad_data)

except ValidationError as e:
    print("[!] SECURITY GUARD ACTIVE: Pydantic rejected corrupt data at the door!")
    print(e)
