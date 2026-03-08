from fastapi import APIRouter
from app.models.patient_model import Patient
from app.services.triage_service import triage_patient
from app.services.queue_service import add_patient
from app.database import patients_collection
import time

router = APIRouter(prefix="/patients")

@router.post("/register")
def register_patient(p: Patient):

    triage = triage_patient(p.symptoms)

    patient = {
        "name": p.name,
        "age": p.age,
        "symptoms": p.symptoms,
        "severity": triage["severity"],
        "arrival_time": time.time()
    }

    # insert into MongoDB
    result = patients_collection.insert_one(patient)

    # convert MongoDB ObjectId to string
    patient["_id"] = str(result.inserted_id)

    queue = add_patient(patient)

    return {
        "patient": patient,
        "queue": queue
    }