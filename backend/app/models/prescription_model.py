
from pydantic import BaseModel
from typing import List

class Prescription(BaseModel):
    patient_id: str
    doctor_id: str
    medicines: List[str]
    notes: str
