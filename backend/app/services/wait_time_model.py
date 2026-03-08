import pandas as pd
import os
from sklearn.linear_model import LinearRegression

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

dataset_path = os.path.join(BASE_DIR, "ai_engine", "dataset", "wait_time.csv")

data = pd.read_csv(dataset_path)

X = data[["queue_size"]]
y = data["wait_time"]

model = LinearRegression()
model.fit(X, y)


def predict_wait_time(queue_size):

    prediction = model.predict([[queue_size]])

    return int(prediction[0])