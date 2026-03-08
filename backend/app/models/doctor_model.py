
from pydantic import BaseModel

class Doctor(BaseModel):
    name: str
    specialization: str
