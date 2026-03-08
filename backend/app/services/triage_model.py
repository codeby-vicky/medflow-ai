from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Example symptom vector model

X = [
[1,0,0,1],
[0,1,0,0],
[0,0,1,1],
[1,1,0,0]
]

y = ["Emergency","Low","Medium","High"]

model = DecisionTreeClassifier()
model.fit(X,y)


def predict_severity(symptoms):

    vector = [
        int("chest pain" in symptoms),
        int("fever" in symptoms),
        int("headache" in symptoms),
        int("breathing difficulty" in symptoms)
    ]

    return model.predict([vector])[0]