from fastapi import APIRouter
from app.database import prescriptions_collection

router = APIRouter(prefix="/history")


@router.get("/{patient_name}")
def patient_history(patient_name: str):

    history = list(
        prescriptions_collection.find(
            {"patient": patient_name},
            {"_id":0}
        )
    )

    return history