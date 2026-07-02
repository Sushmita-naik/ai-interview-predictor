import os
from datetime import datetime


REPORT_FOLDER = "uploads/reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def generate_report(
    candidate_name,
    placement_probability,
    predicted_salary,
    interview_score,
    skills,
    missing_skills,
    recommendations
):
    """
    Generate candidate report
    """

    report_content = f"""
=========================================
        AI INTERVIEW PREDICTOR REPORT
=========================================

Generated On:
{datetime.now()}

Candidate Name:
{candidate_name}

-----------------------------------------
PLACEMENT ANALYSIS
-----------------------------------------

Placement Probability:
{placement_probability}%

Predicted Salary:
{predicted_salary} LPA

Interview Score:
{interview_score}/100

-----------------------------------------
SKILL ANALYSIS
-----------------------------------------

Current Skills:
{", ".join(skills)}

Missing Skills:
{", ".join(missing_skills)}

-----------------------------------------
RECOMMENDATIONS
-----------------------------------------

"""

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):
        report_content += (
            f"{index}. {recommendation}\n"
        )

    report_content += """

-----------------------------------------
FINAL ASSESSMENT
-----------------------------------------

Keep improving technical skills,
projects, and interview preparation.

=========================================
END OF REPORT
=========================================
"""

    filename = (
        f"{candidate_name}_report.txt"
    )

    file_path = os.path.join(
        REPORT_FOLDER,
        filename
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report_content)

    return {
        "filename": filename,
        "file_path": file_path,
        "message": "Report generated successfully"
    }