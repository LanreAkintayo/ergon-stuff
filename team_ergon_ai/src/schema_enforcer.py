from llm_client import LocalLLMClient
from pydantic import BaseModel
import re

class ReservoirInterval(BaseModel):
    well_name: str
    formation: str
    depth_ft: float
    porosity: float
    is_hydrocarbon_bearing: bool


def create_system_prompt(schema_dict: dict) -> str:
    """Transforms Pydantic schema into LLM System Prompt"""

    return f"""
    You are a strict data validation engine.
    Your task is to analyze the text provided by the user and extract information that strictly conforms to the following JSON schema.

    # STRICT JSON SCHEMA DEFINITION
    {schema_dict}

    RULES:
    1. ONLY return valid JSON.
    2. If a field is missing in the text, return null for that field.
    3. Do not include explanations, commentary, or text outside the JSON object.
    4. If the input text contains multiple entities, return a JSON array.
    """
    
def clean_llm_json(raw_text: str) -> str:
    """Strip markdown and non-JSON noise from LLM response"""

    start_index = raw_text.find("{")
    end_index = raw_text.rfind("}")

    if start_index != -1 and end_index != -1:
        text = raw_text[start_index: end_index + 1]
    else:
        text = raw_text 
    
    # remove trailing commas before closing bracket
    text = re.sub(r",\s*}", "}", text)
    text = re.sub(r",\s*]", "]", text)

    return text

def extract_reservoir_data(raw_prompt: str) -> ReservoirInterval:
    # Initialize client
    client = LocalLLMClient()
    
     # Build system prompt
    schema = ReservoirInterval.model_json_schema()
    system_prompt = create_system_prompt(schema)
     
    # Let's generate stuff
    raw_response = client.generate(raw_prompt, system=system_prompt)
    print(f"Raw Response: \n {raw_response}\n")
     
    # Clean the raw response
    clean_response = clean_llm_json(raw_response)
    print(f"Cleaned Response: \n {clean_response}\n")
     
    # Parse to Pydantic
    return ReservoirInterval.model_validate_json(clean_response)



if __name__ == "__main__":
    sample_report = """
Well Bonga-04ST penetrated the main reservoir zone at 9420.0 ft true vertical depth 
within the Agbada Sandstone Formation. Comprehensive petrophysical evaluation 
confirmed clean hydrocarbon-bearing sandstone with an effective porosity of 0.268.
"""
    data = extract_reservoir_data(sample_report)
    print("Well name: ", data.well_name)
    print("Formation: ", data.formation)
    print("Depth: ", data.depth_ft)
    print("Porosity: ", data.porosity)
    print("Hydrocarbon Bearing: ", data.is_hydrocarbon_bearing)
    
    print(data.model_dump_json(indent=2))
