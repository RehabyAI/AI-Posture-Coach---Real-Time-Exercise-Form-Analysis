from fastapi import APIRouter, HTTPException
import json
import os
import random
from datetime import datetime, timedelta
from typing import List

# Import the schemas you just built!
from schemas.analytics import TrendData, ErrorFrequency

# We use the /patient prefix to match your task list perfectly
router = APIRouter(prefix="/patient", tags=["Patient Analytics"])

DB_FILE = "patients_db.json"

# --- 1. THE FAKE DATABASE GENERATOR ---
def load_or_create_db():
    if not os.path.exists(DB_FILE):
        db = {}
        possible_errors = ["Left shoulder dropped", "Pacing too fast", "Incomplete range of motion", "Back bent"]
        
        # Create 5 fake patients
        for i in range(1, 6):
            patient_id = f"pat_00{i}"
            sessions = []
            
            # Create 10 fake sessions for each patient
            for j in range(10):
                # Generate dates going backwards from today
                date_str = (datetime.now() - timedelta(days=(10-j))).strftime("%Y-%m-%d")
                sessions.append({
                    "session_id": f"sess_00{j+1}",
                    "date": date_str,
                    "score": round(random.uniform(70.0, 95.0), 1), # Random score between 70 and 95
                    "main_error": random.choice(possible_errors)
                })
            db[patient_id] = {"patient_info": {"name": f"Patient {i}"}, "sessions": sessions}
            
        # Save to JSON storage
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(db, f, indent=4)
            
    # Load and return the JSON data
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Load the database into memory when the server starts
db = load_or_create_db()


# --- 2. THE ENDPOINTS ---

@router.get("/{id}/history")
def get_patient_history(id: str):
    """Returns all 10 past sessions for a patient."""
    if id not in db:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"patient_id": id, "history": db[id]["sessions"]}

@router.get("/{id}/trends", response_model=List[TrendData])
def get_patient_trends(id: str):
    """Returns score trends for charting."""
    if id not in db:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Map the JSON data to your Pydantic schema
    trends = []
    for s in db[id]["sessions"]:
        trends.append(TrendData(date=s["date"], average_score=s["score"]))
    return trends

@router.get("/{id}/errors", response_model=List[ErrorFrequency])
def get_patient_errors(id: str):
    """Calculates and returns the most frequent physical errors."""
    if id not in db:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Count how many times each error happened
    error_tally = {}
    for s in db[id]["sessions"]:
        error_name = s["main_error"]
        error_tally[error_name] = error_tally.get(error_name, 0) + 1
        
    # Map the tally to your Pydantic schema
    error_list = []
    for name, count in error_tally.items():
        error_list.append(ErrorFrequency(error_name=name, occurrence_count=count))
        
    return error_list