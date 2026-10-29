depths = [8900, 8950, 9000, 9050, 9100, 9150, 9200]
formations = ["Benin Sand", "Upper Agbada", "Main Pay Sand", "Lower Agbada"]


total_stations = len(depths)
shallowest = depths[0]
last = depths[-1]

pay_zone_depths = depths[2:5]
formations.append("Akata Shale")

print(f"""
      Total Depth stations recorded: {total_stations}
      Shallowest Depth: {shallowest}
      Pay Zone Depth: {pay_zone_depths}
      New formations list: {formations}
""")