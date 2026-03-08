import ollama

MODEL = "phi3:mini"

def ai_diagnose(symptoms):

    symptom_text = ", ".join(symptoms)

    prompt = f"""
You are an AI clinical assistant.

Patient symptoms:
{symptom_text}

Provide:
1. Possible diseases
2. Severity (Low / Medium / High / Emergency)
3. Recommended next step

Keep the answer short.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": 0.2,
            "num_predict": 150
        }
    )

    return response["message"]["content"]