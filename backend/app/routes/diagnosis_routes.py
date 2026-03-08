from fastapi import APIRouter
from app.services.ai_diagnosis_service import ai_diagnose

router = APIRouter(prefix="/diagnosis")


@router.post("/predict")
def predict(data: dict):

    symptoms = data["symptoms"]

    result = ai_diagnose(symptoms)

    return {
        "analysis": result
    }