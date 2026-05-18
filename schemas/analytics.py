from pydantic import BaseModel, Field
from typing import List

class TrendData(BaseModel):
    date: str = Field(..., example="2026-05-15")
    average_score: float = Field(..., example=85.5)

class ErrorFrequency(BaseModel):
    error_name: str = Field(..., example="Left shoulder dropped")
    occurrence_count: int = Field(..., example=12)

class ExerciseStats(BaseModel):
    exercise_name: str = Field(..., example="Shoulder Raise")
    total_sessions: int = Field(..., example=5)
    overall_average_score: float = Field(..., example=82.0)

class PatientAnalytics(BaseModel):
    patient_id: str = Field(..., example="pat_12345")
    total_completed_sessions: int = Field(..., example=14)
    global_average_score: float = Field(..., example=84.2)
    performance_trends: List[TrendData]
    top_common_errors: List[ErrorFrequency]
    exercise_breakdown: List[ExerciseStats]
    recovery_status: str = Field(..., example="Improving steadily")