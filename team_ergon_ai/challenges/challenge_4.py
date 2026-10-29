chunks = [
    {
        "chunk_id": "chunk_01",
        "lithology": "Shale",
        "porosity": 0.05,
        "description": "Dense, impermeable marine sealing shale."
    },
    {
        "chunk_id": "chunk_02",
        "lithology": "Sandstone",
        "porosity": 0.24,
        "description": "Coarse reservoir sandstone with oil shows."
    },
    {
        "chunk_id": "chunk_03",
        "lithology": "Siltstone",
        "porosity": 0.12,
        "description": "Tight siltstone with low permeability."
    },
    {
        "chunk_id": "chunk_04",
        "lithology": "Sandstone",
        "porosity": 0.28,
        "description": "Massive channel sandstone exhibiting high primary porosity."
    }
]


pay_zones = []
pay_porosities = []


for chunk in chunks:
    if chunk["lithology"] == "Sandstone" and chunk["porosity"] > 0.2:
        pay_zones.append(chunk["chunk_id"])
        pay_porosities.append(chunk["porosity"])
        
        
avg_porosity = sum(pay_porosities) / len(pay_porosities)

print(pay_zones)
print(round(avg_porosity, 2))