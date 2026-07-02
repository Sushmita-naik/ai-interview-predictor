from pydantic import BaseModel
from typing import List


class ResumeUploadResponse(BaseModel):
    message: str
    filename: str
    filepath: str


class ResumeAnalysisRequest(BaseModel):
    resume_text: str


class ResumeAnalysisResponse(BaseModel):
    skills: List[str]
    projects: List[str]
    education: List[str]
    experience: List[str]


class SkillExtractionResponse(BaseModel):
    extracted_skills: List[str]


class ResumeScoreResponse(BaseModel):
    resume_score: float
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]