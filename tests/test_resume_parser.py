import requests

BASE_URL = "http://localhost:8000"


def test_resume_upload():
    try:
        with open("sample_resume.pdf", "rb") as file:
            files = {
                "resume": file
            }

            response = requests.post(
                f"{BASE_URL}/upload-resume",
                files=files
            )

            print("\nResume Upload Response:")
            print(response.json())

            assert response.status_code == 200

    except FileNotFoundError:
        print(
            "sample_resume.pdf not found. "
            "Skipping upload test."
        )


def test_resume_analysis():
    payload = {
        "resume_text": """
        Python Developer with React,
        Machine Learning, SQL and FastAPI.
        Built AI Interview Predictor project.
        """
    }

    response = requests.post(
        f"{BASE_URL}/analyze-resume",
        json=payload
    )

    print("\nResume Analysis Response:")
    print(response.json())

    assert response.status_code == 200


def test_skill_extraction():
    payload = {
        "resume_text": """
        Skills:
        Python, React, SQL, Machine Learning,
        FastAPI, GitHub
        """
    }

    response = requests.post(
        f"{BASE_URL}/extract-skills",
        json=payload
    )

    print("\nSkill Extraction Response:")
    print(response.json())

    assert response.status_code == 200


def test_placement_prediction():
    payload = {
        "cgpa": 8.5,
        "internships": 2,
        "projects": 4,
        "certifications": 3,
        "technical_score": 85,
        "communication_score": 80,
        "github_score": 78
    }

    response = requests.post(
        f"{BASE_URL}/predict-placement",
        json=payload
    )

    print("\nPlacement Prediction Response:")
    print(response.json())

    assert response.status_code == 200


if __name__ == "__main__":
    print("Running Resume Parser Tests...\n")

    test_resume_upload()
    test_resume_analysis()
    test_skill_extraction()
    test_placement_prediction()

    print("\nAll Resume Tests Completed Successfully")