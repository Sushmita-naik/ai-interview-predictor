from pydantic import BaseModel
from typing import List


class InterviewQuestionRequest(BaseModel):
    skills: List[str]
    projects: List[str]


class InterviewAnswer(BaseModel):
    question: str
    answer: str


class InterviewSubmission(BaseModel):
    candidate_name: str
    answers: List[InterviewAnswer]


class InterviewScoreRequest(BaseModel):
    technical_score: float
    communication_score: float
    project_score: float
    confidence_score: float


class InterviewScoreResponse(BaseModel):
    total_score: float
    grade: str