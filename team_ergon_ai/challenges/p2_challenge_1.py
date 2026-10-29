import json


well_summary = {
    "well_name": "Egina-Deep-02",
    "block": "OML-130",
    "water_depth_m": 1550,
    "reservoir_targets": ["Upper Miocene", "Middle Miocene", "Lower Turbidite"],
    "metrics": {
        "avg_porosity": 0.275,
        "permeability_md": 620.0,
        "hydrocarbon_type": "Light Crude"
    },
    "is_producing": True
}


with open("egina_summary.json", "w", encoding="utf-8") as f:
    json.dump(well_summary, f, indent=4)
    
print(f"[+] File {f.name} successfully written to disk!")

# Now let's read to memory
with open(f.name, "r", encoding="utf-8") as read_f:
    verified_data = json.load(read_f)
    
print(verified_data["well_name"]) 
print(verified_data["metrics"]["avg_porosity"]) 