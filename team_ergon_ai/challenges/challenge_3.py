chunk = {
    "chunk_id": "oml_42_p12_c03",
    "well": "Jones-Creek-07",
    "porosity": 0.26,
    "lithology": "Sandstone",
    "text": "The reservoir section shows clean sandstone with high porosity of 26% and good oil shows."
}


well_name = chunk["well"]
operator_name = chunk.get("operator", "NNPC / Chevron Joint Venture")

chunk["is_reservoir"] = chunk["porosity"] >= 0.20
citation = f"Citation: {well_name} (ID: {chunk["chunk_id"]}) | Operator: {operator_name}"


print(operator_name)
print(chunk)
print(citation)