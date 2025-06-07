from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("fraud_model.pkl")

class Transaction(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(transaction: Transaction):
    prediction = model.predict([np.array(transaction.features)])
    return {"prediction": int(prediction[0])}
