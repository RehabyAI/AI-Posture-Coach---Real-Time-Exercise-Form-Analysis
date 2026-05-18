import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_FILE = os.path.join(BASE_DIR, "storage", "db.json")


def read_db():
    if not os.path.exists(DB_FILE):
        return {"patients": [], "sessions": []}
    with open(DB_FILE, "r") as file:
        return json.load(file)


def write_db(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_patient(patient_data: dict):
    db = read_db()
    db["patients"].append(patient_data)
    write_db(db)
    return patient_data


def add_session(session_data: dict):
    db = read_db()
    db["sessions"].append(session_data)
    write_db(db)
    return session_data