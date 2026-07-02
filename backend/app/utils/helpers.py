import re
import os
from datetime import datetime


def calculate_percentage(score, total):
    """
    Calculate percentage
    """

    if total == 0:
        return 0

    return round((score / total) * 100, 2)


def generate_grade(score):
    """
    Generate grade from score
    """

    if score >= 90:
        return "A+"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 50:
        return "D"

    return "F"


def sanitize_filename(filename):
    """
    Remove unsafe characters from filename
    """

    return re.sub(
        r'[^a-zA-Z0-9_.-]',
        '_',
        filename
    )


def allowed_file(filename):
    """
    Check allowed resume formats
    """

    allowed_extensions = {
        "pdf",
        "doc",
        "docx"
    }

    return (
        "." in filename and
        filename.rsplit(
            ".",
            1
        )[1].lower() in allowed_extensions
    )


def get_timestamp():
    """
    Current timestamp
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def calculate_interview_score(
    technical_score,
    communication_score,
    project_score,
    confidence_score
):
    """
    Calculate final interview score
    """

    total = (
        technical_score +
        communication_score +
        project_score +
        confidence_score
    ) / 4

    return round(total, 2)


def generate_report_filename(
    candidate_name
):
    """
    Generate report filename
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    clean_name = (
        candidate_name
        .replace(" ", "_")
    )

    return (
        f"{clean_name}_"
        f"{timestamp}.txt"
    )


def file_exists(path):
    """
    Check file existence
    """

    return os.path.exists(path)


def safe_int(value, default=0):
    """
    Safe integer conversion
    """

    try:
        return int(value)

    except Exception:
        return default


def safe_float(value, default=0.0):
    """
    Safe float conversion
    """

    try:
        return float(value)

    except Exception:
        return default


if __name__ == "__main__":

    print(
        calculate_percentage(
            85,
            100
        )
    )

    print(
        generate_grade(
            85
        )
    )

    print(
        sanitize_filename(
            "Sushmita Resume.pdf"
        )
    )

    print(
        generate_report_filename(
            "Sushmita Naik"
        )
    )