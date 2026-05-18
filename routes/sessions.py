from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter

from schemas.session import Session, SessionCreate
from services.storage_service import add_session, read_db

router = APIRouter(prefix="/sessions", tags=["Sessions"])


@router.post("/", response_model=Session)
def log_session(session: SessionCreate):
    new_session = {
        "session_id": f"sess_{uuid4().hex[:8]}",
        **session.model_dump(),
        "start_time": datetime.utcnow(),
        "end_time": datetime.utcnow(),
    }
    return add_session(new_session)


@router.get("/")
def get_sessions():
    return read_db().get("sessions", [])