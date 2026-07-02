from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads/resumes"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(
    resume: UploadFile = File(...)
):
    file_path = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    with open(file_path, "wb") as buffer:
        content = await resume.read()
        buffer.write(content)

    return {
        "message": "Resume uploaded successfully",
        "filename": resume.filename,
        "filepath": file_path
    }


@router.post("/analyze-resume")
def analyze_resume(data: dict):

    resume_text = data.get(
        "resume_text",
        ""
    )

    skills = []

    skill_keywords = [
        "Python",
        "Java",
        "C++",
        "React",
        "Node.js",
        "FastAPI",
        "SQL",
        "MongoDB",
        "Machine Learning",
        "Deep Learning",
        "AWS",
        "Docker",
        "Git"
    ]

    for skill in skill_keywords:
        if skill.lower() in resume_text.lower():
            skills.append(skill)

    return {
        "skills": skills,
        "resume_score": min(
            len(skills) * 10,
            100
        )
    }


@router.post("/extract-skills")
def extract_skills(data: dict):

    resume_text = data.get(
        "resume_text",
        ""
    )

    extracted_skills = []

    skill_keywords = [
        "Python",
        "Java",
        "C++",
        "React",
        "Node.js",
        "FastAPI",
        "SQL",
        "MongoDB",
        "Machine Learning",
        "Deep Learning",
        "AWS",
        "Docker",
        "Git"
    ]

    for skill in skill_keywords:
        if skill.lower() in resume_text.lower():
            extracted_skills.append(skill)

    return {
        "extracted_skills":
            extracted_skills
    }


@router.post("/resume-score")
def resume_score(data: dict):

    skills = data.get(
        "skills",
        []
    )

    score = min(
        len(skills) * 10,
        100
    )

    return {
        "resume_score": score,
        "strengths": skills,
        "recommendations": [
            "Add more projects",
            "Improve GitHub profile",
            "Learn cloud technologies"
        ]
    }