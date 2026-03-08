
def suggest_disease(symptoms):
    if "chest pain" in symptoms:
        return "Possible Cardiac Issue"
    if "fever" in symptoms and "cough" in symptoms:
        return "Possible Flu"
    return "General Infection"
