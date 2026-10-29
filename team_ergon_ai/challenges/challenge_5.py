def assemble_rag_prompt(well_name, question, retrieved_context):
    if not retrieved_context or not retrieved_context.strip():
        return "DATA UNAVAILABLE: No relevant geological context found"
    
    return f"""
        TARGET WELL: {well_name}
        CONTEXT: {retrieved_context.strip()}
        QUESTION: {question}
        RULE: Answer strictly using facts from the CONTEXT. Do not hallucinate.
    """ 


result1 = assemble_rag_prompt("Bonga-01", "What is porosity?", "")
result2 = assemble_rag_prompt("Bonga-01", "What is porosity?", "Sandstone interval has 24% porosity.") 

print(result1)
print(result2)