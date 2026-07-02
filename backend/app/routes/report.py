from fastapi import APIRouter
import os

router = APIRouter()

REPORT_FOLDER = "uploads/reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


@router.post("/generate-report")
def generate_report(data: dict):

    candidate_name = data.get(
        "candidate_name",
        "Unknown"
    )

    placement_probability = data.get(
        "placement_probability",
        0
    )

    predicted_salary = data.get(
        "predicted_salary_lpa",
        0
    )

    interview_score = data.get(
        "interview_score",
        0
    )

    recommended_skills = data.get(
        "recommended_skills",
        []
    )

    report_content = f"""
Candidate Name: {candidate_name}

Placement Probability:
{placement_probability}%

Predicted Salary:
{predicted_salary} LPA

Interview Score:
{interview_score}/100

Recommended Skills:
{", ".join(recommended_skills)}

Overall Assessment:
Candidate shows good potential for placement.
"""

    report_path = os.path.join(
        REPORT_FOLDER,
        f"{candidate_name}_report.txt"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report_content)

    return {
        "message":
            "Report generated successfully",
        "report_path":
            report_path
    }


@router.get("/reports")
def get_reports():

    reports = os.listdir(
        REPORT_FOLDER
    )

    return {
        "reports": reports
    }