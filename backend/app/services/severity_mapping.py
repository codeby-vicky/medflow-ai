# severity_mapping.py

# symptom keywords mapped to severity
symptom_severity = {

    # EMERGENCY
    "chest pain": "Emergency",
    "severe chest pain": "Emergency",
    "unconscious": "Emergency",
    "difficulty breathing": "Emergency",
    "shortness of breath": "Emergency",
    "stroke": "Emergency",
    "seizure": "Emergency",

    # HIGH
    "covid": "High",
    "high fever": "High",
    "persistent fever": "High",
    "dengue": "High",
    "malaria": "High",
    "vomiting blood": "High",
    "severe dehydration": "High",

    # MEDIUM
    "migraine": "Medium",
    "headache": "Medium",
    "stomach pain": "Medium",
    "gastritis": "Medium",
    "food poisoning": "Medium",
    "moderate fever": "Medium",

    # LOW
    "cold": "Low",
    "common cold": "Low",
    "flu": "Low",
    "influenza": "Low",
    "sneezing": "Low",
    "runny nose": "Low",
    "allergy": "Low",
    "sore throat": "Low"
}


priority_rank = {
    "Emergency": 4,
    "High": 3,
    "Medium": 2,
    "Low": 1
}


def get_severity(symptoms):

    # symptoms come as list
    text = " ".join(symptoms).lower()

    detected = "Low"

    for key in symptom_severity:

        if key in text:

            sev = symptom_severity[key]

            if priority_rank[sev] > priority_rank[detected]:
                detected = sev

    return detected