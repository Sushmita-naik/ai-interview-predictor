from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db import create_tables

from app.routes.auth import router as auth_router
from app.routes.interview import router as interview_router
from app.routes.resume import router as resume_router
from app.routes.report import router as report_router

# Create database tables
create_tables()

app = FastAPI(
    title="AI Interview Predictor API",
    description="AI-powered Interview Preparation Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "AI Interview Predictor Backend Running Successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

# Register Routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(interview_router, prefix="/interview", tags=["Interview"])
app.include_router(resume_router, prefix="/resume", tags=["Resume"])
app.include_router(report_router, prefix="/report", tags=["Report"])