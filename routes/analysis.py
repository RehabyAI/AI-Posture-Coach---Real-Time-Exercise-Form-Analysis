from fastapi import APIRouter
from pydantic import BaseModel

# THIS is the exact line your server is crying out for!
router = APIRouter(prefix="/analysis", tags=["Analysis"])

class FrameRequest(BaseModel):
    image_base64: str

@router.post("/frame")
def analyze_frame(request: FrameRequest):
    return {
        "score": 88,
        "status": "Good",
        "feedback": "Posture looks great! Keep it up."
    }