
from fastapi import APIRouter
from app.services.triage_service import triage_patient

router = APIRouter(prefix="/triage")

@router.post("/")
def triage(data: dict):
    symptoms = data.get("symptoms",[])
    return triage_patient(symptoms)
