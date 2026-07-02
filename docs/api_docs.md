# AI Interview Predictor API Documentation

## Base URL

http://localhost:8000

---

## Authentication APIs

### Register User

**POST** `/register`

Request:

```json
{
  "name": "Sushmita Naik",
  "email": "sushmita@gmail.com",
  "password": "123456"
}
```

Response:

```json
{
  "message": "User registered successfully"
}
```

---

### Login User

**POST** `/login`

Request:

```json
{
  "email": "sushmita@gmail.com",
  "password": "123456"
}
```

Response:

```json
{
  "message": "Login successful",
  "token": "dummy_token_123"
}
```

---

## Resume APIs

### Upload Resume

**POST** `/upload-resume`

Response:

```json
{
  "message": "Resume uploaded successfully",
  "filename": "resume.pdf"
}
```

---

### Analyze Resume

**POST** `/analyze-resume`

Request:

```json
{
  "resume_text": "Python React SQL Machine Learning"
}
```

Response:

```json
{
  "skills": [
    "Python",
    "React",
    "SQL"
  ],
  "resume_score": 75
}
```

---

## Interview APIs

### Generate Questions

**POST** `/generate-questions`

Request:

```json
{
  "skills": ["Python", "React"],
  "projects": ["AI Interview Predictor"]
}
```

Response:

```json
{
  "questions": [
    "What are Python decorators?",
    "Explain React Hooks."
  ]
}
```

---

### Submit Interview

**POST** `/submit-interview`

Response:

```json
{
  "message": "Interview submitted successfully"
}
```

---

### Interview Score

**POST** `/interview-score`

Request:

```json
{
  "technical_score": 85,
  "communication_score": 80,
  "project_score": 90,
  "confidence_score": 75
}
```

Response:

```json
{
  "total_score": 82.5,
  "grade": "Good"
}
```

---

## Report APIs

### Generate Report

**POST** `/generate-report`

Response:

```json
{
  "message": "Report generated successfully"
}
```

---

## Health Check

**GET** `/health`

Response:

```json
{
  "status": "healthy",
  "server": "running"
}
```

---

## Technologies Used

### Frontend

* React
* Axios
* React Router

### Backend

* FastAPI
* SQLite
* PyMuPDF

### Machine Learning

* Pandas
* NumPy
* Scikit-Learn
* Joblib

---

Version: 1.0.0
