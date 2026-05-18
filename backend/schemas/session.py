from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class SessionCreate(BaseModel):
    patient_id: str
    exercise_name: str
    rep_count: int
    average_score: float
    errors_detected: List[str]
    feedback_summary: str


class Session(SessionCreate):
    session_id: str
    start_time: datetime
    end_time: Optional[datetime] = None