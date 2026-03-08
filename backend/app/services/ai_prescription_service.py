import ollama

MODEL = "phi3:mini"

def suggest_medicine(diagnosis):

    prompt = f"""
You are a medical assistant.

Diagnosis:
{diagnosis}

Suggest 2–3 common medicines typically used for this condition.

Return only medicine names and dosage examples.

Example:
Paracetamol 500mg
Ibuprofen 200mg
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role":"user","content":prompt}],
        options={"temperature":0.2,"num_predict":120}
    )

    return response["message"]["content"]