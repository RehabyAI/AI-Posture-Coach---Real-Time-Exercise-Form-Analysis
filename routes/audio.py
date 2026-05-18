from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from gtts import gTTS
import io

router = APIRouter(prefix="/audio", tags=["Audio"])

class AudioRequest(BaseModel):
    text: str
    lang: str = "en"

# CRITICAL FIX: Added response_class=StreamingResponse right here 👇
@router.post("/generate-audio", response_class=StreamingResponse)
def generate_audio(request: AudioRequest):
    # 1. Generate the audio using Google TTS
    tts = gTTS(text=request.text, lang=request.lang, slow=False)
    
    # 2. Save it to an in-memory bytes buffer
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    
    # 3. Rewind the buffer back to the starting point
    audio_buffer.seek(0)
    
    # 4. Stream the MP3 file securely
    return StreamingResponse(
        audio_buffer, 
        media_type="audio/mpeg",
        headers={"Content-Disposition": "attachment; filename=speech.mp3"}
    )