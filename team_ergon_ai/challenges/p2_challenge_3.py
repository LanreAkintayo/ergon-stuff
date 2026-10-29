import json

raw_ai_response = '{"well": "Usan-West-01", "formation": "Agbada Sand", "porosity_est": 0.25, "verdict": "Commercial Pay"}'

response_dict = json.loads(raw_ai_response)

print(raw_ai_response)
print(response_dict)

print(type(raw_ai_response))
print(type(response_dict))

response_dict["confidence_score"] = 0.94
response_dict["reviewed_by"] = "Team Ergon AI"

pretty_json_str = json.dumps(response_dict, indent=2)
print(pretty_json_str)