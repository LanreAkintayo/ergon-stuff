well_name = "Bonga-Southwest-03"
field_name = "Bonga Deepwater"
raw_depth = "10450"
water_saturation = 0.28
is_commercial = True

depth_ft = int(raw_depth)
target_depth = depth_ft + 500

oil_saturation = (1.0 - water_saturation) * 100

print(f"""
      Well Name: {well_name}
      Current Depth: {raw_depth}
      Target Depth: {target_depth}
      Oil Saturation: {round(oil_saturation, 1)}
      Commercial Viability: {is_commercial} 
""")
