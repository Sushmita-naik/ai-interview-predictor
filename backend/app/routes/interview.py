from fastapi import APIRouter

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)

@router.get("/")
def interview_home():
    return {"message": "Interview API is running"}

@router.post("/start")
def start_interview():
    return {
        "message": "Interview started",
        "questions": [
            "Tell me about yourself",
            "What is Python?",
            "Explain your project"
        ]
    }

@router.post("/submit")
def submit_interview():
    return {
        "message": "Interview submitted",
        "score": 85
    }