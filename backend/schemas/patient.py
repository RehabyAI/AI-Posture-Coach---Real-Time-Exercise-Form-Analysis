from datetime import datetime

from pydantic import BaseModel


class PatientCreate(BaseModel):
    full_name: str
    age: int
    gender: str
    condition: str
    rehab_plan: str


class Patient(PatientCreate):
    patient_id: str
    created_at: datetime