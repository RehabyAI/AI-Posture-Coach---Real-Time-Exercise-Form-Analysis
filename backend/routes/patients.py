from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter

from schemas.patient import Patient, PatientCreate
from services.storage_service import add_patient, read_db

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/", response_model=Patient)
def create_patient(patient: PatientCreate):
    new_patient = {
        "patient_id": f"pat_{uuid4().hex[:8]}",
        **patient.model_dump(),
        "created_at": datetime.utcnow(),
    }
    return add_patient(new_patient)


@router.get("/")
def get_patients():
    return read_db().get("patients", [])