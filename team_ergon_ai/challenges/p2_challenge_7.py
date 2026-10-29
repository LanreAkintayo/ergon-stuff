import pandas as pd
import numpy as np 

# Create and save raw_wells.csv
raw_data = {
    "well_id": ["Well-A", "Well-B", "Well-C", "Well-D", "Well-E"],
    "depth_ft": [8900, 9150, 9300, 9450, 9600],
    "lithology": ["Shale", "Sandstone", "Sandstone", "Limestone", "Sandstone"],
    "porosity": [0.06, 0.25, -999.25, 0.12, 0.28],   # ⚠️ Well-C has corrupt -999.25 sensor error!
    "permeability_md": [2.5, 480.0, 310.0, 45.0, 520.0]
}
raw_df = pd.DataFrame(raw_data)
raw_df.to_csv("raw_wells.csv", index=False)

# Load raw_wells.csv
df = pd.read_csv("raw_wells.csv")
print(df)


# Clean the oilfield sensor error code
df.replace(-999.25, np.nan, inplace=True)

avg_poro = df["porosity"].mean()
print(round(avg_poro, 3))

# Filter prime reservoir targets
reservoir_mask = (df["lithology"] == "Sandstone") & (df["porosity"] >= 0.20)
prime_df = df[reservoir_mask]

print(prime_df[["well_id", "depth_ft", "porosity"]])

# Export the filtered table
prime_df.to_csv("prime_reservoirs.csv", index=False)

print("[+] Saved prime reservoir wells to prime_reservoirs.csv!")