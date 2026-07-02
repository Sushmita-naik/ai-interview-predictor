import requests

BASE_URL = "http://localhost:8000"


def test_home():
    response = requests.get(f"{BASE_URL}/")

    assert response.status_code == 200

    print("Home API Test Passed")


def test_register():
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "123456"
    }

    response = requests.post(
        f"{BASE_URL}/register",
        json=payload
    )

    print("Register Response:")
    print(response.json())

    assert response.status_code in [200, 201]


def test_login():
    payload = {
        "email": "test@example.com",
        "password": "123456"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    print("Login Response:")
    print(response.json())

    assert response.status_code == 200


def test_resume_upload():
    file_path = "sample_resume.pdf"

    try:
        with open(file_path, "rb") as file:
            files = {
                "resume": file
            }

            response = requests.post(
                f"{BASE_URL}/upload-resume",
                files=files
            )

            print("Upload Response:")
            print(response.json())

            assert response.status_code == 200

    except FileNotFoundError:
        print(
            "sample_resume.pdf not found. "
            "Skipping upload test."
        )


if __name__ == "__main__":
    print("Running API Tests...\n")

    test_home()
    test_register()
    test_login()
    test_resume_upload()

    print("\nAll Tests Completed")