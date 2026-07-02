from pydantic import BaseModel


class PlacementPredictionRequest(BaseModel):
    cgpa: float
    internships: int
    projects: int
    certifications: int
    technical_score: float
    communication_score: float
    github_score: float


class PlacementPredictionResponse(BaseModel):
    placement_probability: float
    placement_status: str


class SalaryPredictionResponse(BaseModel):
    predicted_salary_lpa: float


class SkillRecommendationResponse(BaseModel):
    current_skills: list[str]
    missing_skills: list[str]
    recommended_skills: list[str]


class FinalReportResponse(BaseModel):
    candidate_name: str
    placement_probability: float
    predicted_salary_lpa: float
    interview_score: float
    recommended_skills: list[str]
    report_summary: str