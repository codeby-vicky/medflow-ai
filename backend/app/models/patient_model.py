
from pydantic import BaseModel
from typing import List

class Patient(BaseModel):
    name: str
    age: int
    symptoms: List[str]
