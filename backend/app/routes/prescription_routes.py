from fastapi import APIRouter
from app.services.prescription_service import create_prescription, get_prescriptions
from app.services.ai_prescription_service import suggest_medicine

router = APIRouter(prefix="/prescriptions")


@router.post("/create")
def add_prescription(data: dict):

    patient = data["patient"]
    diagnosis = data["diagnosis"]
    medicines = data["medicines"]

    result = create_prescription(patient, diagnosis, medicines)

    return {"prescription": result}


@router.get("/list")
def list_prescriptions():

    return get_prescriptions()

@router.post("/suggest")

def ai_suggest(data: dict):

    diagnosis = data["diagnosis"]

    medicines = suggest_medicine(diagnosis)

    return {"medicines": medicines}