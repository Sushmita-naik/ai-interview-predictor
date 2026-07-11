import requests

BASE_URL = "http://localhost:8000"


def test_generate_questions():
    payload = {
        "skills": [
            "Python",
            "React",
            "Machine Learning"
        ],
        "projects": [
            "AI Interview Predictor"
        ]
    }

    response = requests.post(
        f"{BASE_URL}/generate-questions",
        json=payload
    )

    print("\nQuestion Generation Response:")
    print(response.json())

    assert response.status_code == 200


def test_submit_interview():
    payload = {
        "candidate_name": "Test User",
        "answers": [
            {
                "question": "Tell me about yourself",
                "answer": "I am a Computer Science student."
            },
            {
                "question": "Explain your project",
                "answer": "I developed an AI Interview Predictor."
            }
        ]
    }

    response = requests.post(
        f"{BASE_URL}/submit-interview",
        json=payload
    )

    print("\nInterview Submission Response:")
    print(response.json())

    assert response.status_code == 200


def test_interview_score():
    payload = {
        "technical_score": 85,
        "communication_score": 78,
        "project_score": 90,
        "confidence_score": 80
    }

    response = requests.post(
        f"{BASE_URL}/interview-score",
        json=payload
    )

    print("\nInterview Score Response:")
    print(response.json())

    assert response.status_code == 200


if __name__ == "__main__":
    print("Running Interview Tests...\n")

    test_generate_questions()
    test_submit_interview()
    test_interview_score()

    print("\nAll Interview Tests Completed Successfully")
