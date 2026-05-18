from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.health import router as health_router
from routes.patients import router as patients_router
from routes.sessions import router as sessions_router
from routes.analysis import router as analysis_router
from routes.audio import router as audio_router
from routes.analytics import router as analytics_router
from routes.analytics import router as analytics_router

app = FastAPI(title="Rehaby Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(patients_router)
app.include_router(sessions_router)
app.include_router(analysis_router)
app.include_router(audio_router)
app.include_router(analytics_router)
app.include_router(analytics_router)

@app.get("/")
def root():
    return {"message": "Welcome to Rehaby Backend API"}