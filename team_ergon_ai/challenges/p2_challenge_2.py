import json

def load_oilfield_json(filepath: str):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            oilfield_data = json.load(f)
            return oilfield_data
            
    except FileNotFoundError:
        print(f"[!] WARNING: The file `{filepath}` does not exist on disk.")
        return {}
    
    
missing_data = load_oilfield_json("missing_subsurface_file.json")
print("Missing Data: ", missing_data)

egina_data = load_oilfield_json("egina_summary.json")
print(egina_data["well_name"])
print(egina_data["reservoir_targets"])