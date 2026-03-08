import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
dataset_path = os.path.join(BASE_DIR, "ai_engine", "dataset", "Training.csv")

dataset = pd.read_csv(dataset_path)

X = dataset.drop("prognosis", axis=1)
y = dataset["prognosis"]

model = DecisionTreeClassifier()
model.fit(X, y)

symptom_columns = X.columns

def normalize_symptom(symptom):
    return symptom.strip().lower().replace(" ", "_")

symptom_alias = {
    "cold": "runny_nose",
    "sneezing": "continuous_sneezing",
    "fever": "high_fever",
    "cough": "cough",
    "headache": "headache",
    "chest pain": "chest_pain",
    "breathing difficulty": "breathlessness",
    "vomiting": "vomiting",
    "body pain": "muscle_pain",
    "fatigue": "fatigue"
}

def predict_disease(symptoms):

    input_vector = [0] * len(symptom_columns)

    for symptom in symptoms:

        symptom = symptom.strip().lower()

        if symptom in symptom_alias:
            symptom = symptom_alias[symptom]

        if symptom in symptom_columns:
            index = symptom_columns.get_loc(symptom)
            input_vector[index] = 1

    prediction = model.predict([input_vector])

    return prediction[0]