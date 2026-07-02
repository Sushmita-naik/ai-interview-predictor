# AI Interview Predictor Project Flow

## Overview

The AI Interview Predictor analyzes a candidate's resume, skills, projects, and interview performance to predict placement chances, salary range, and provide improvement recommendations.

---

# System Flow

```text
User Registration/Login
            │
            ▼
      Upload Resume
            │
            ▼
      Resume Parsing
            │
            ▼
      Skill Extraction
            │
            ▼
      Project Detection
            │
            ▼
     GitHub Analysis
            │
            ▼
 Interview Question Generation
            │
            ▼
      User Interview
            │
            ▼
      Answer Evaluation
            │
            ▼
     Placement Prediction
            │
            ▼
       Salary Prediction
            │
            ▼
      Report Generation
            │
            ▼
      Final Dashboard
```

---

# Detailed Workflow

## Step 1: User Authentication

User registers and logs into the platform.

Input:

* Name
* Email
* Password

Output:

* User Account Created

---

## Step 2: Resume Upload

User uploads resume in PDF format.

Input:

* Resume PDF

Output:

* Resume Stored

Location:

```text
uploads/resumes/
```

---

## Step 3: Resume Parsing

System extracts information from resume.

Extracted Data:

* Email
* Phone Number
* Skills
* Projects
* Education
* Certifications

Output:

```json
{
  "skills": ["Python", "React"],
  "projects": ["WhatsApp Chat Analyzer"]
}
```

---

## Step 4: GitHub Analysis

User provides GitHub profile.

System analyzes:

* Repository Count
* Languages Used
* Stars
* Project Activity
* Commit Frequency

Output:

```json
{
  "github_score": 82
}
```

---

## Step 5: Interview Question Generation

Questions are generated using:

* Skills
* Projects
* GitHub Repositories

Example:

```text
How did you implement chat filtering in your WhatsApp Chat Analyzer project?

Why did you choose Pandas?
```

---

## Step 6: Interview Process

Candidate answers generated questions.

Features:

* Timer
* Anti-Cheating Detection
* Tab Switch Monitoring
* Copy/Paste Detection

Output:

* Candidate Responses

---

## Step 7: Answer Evaluation

System evaluates:

* Technical Knowledge
* Communication Skills
* Confidence
* Relevance

Output:

```json
{
  "score": 85,
  "feedback": "Strong technical answer"
}
```

---

## Step 8: Placement Prediction

ML Model predicts:

* Placement Probability

Example:

```json
{
  "placement_probability": 87
}
```

---

## Step 9: Salary Prediction

ML Model predicts:

* Expected Salary Package

Example:

```json
{
  "predicted_salary": 8.5
}
```

---

## Step 10: Skill Gap Analysis

System identifies:

* Missing Skills
* Weak Areas
* Recommended Technologies

Example:

```text
Missing Skills:
Docker
AWS
System Design
```

---

## Step 11: Report Generation

Final report includes:

* Resume Score
* GitHub Score
* Interview Score
* Placement Probability
* Salary Prediction
* Recommended Skills

Output:

```text
Candidate_Report.pdf
```

Location:

```text
uploads/reports/
```

---

## Step 12: Dashboard

User views:

* Placement Probability
* Salary Prediction
* Interview Performance
* Skill Recommendations
* Downloadable Report

---

# Technologies Used

## Frontend

* React.js
* Axios
* React Router
* CSS

## Backend

* FastAPI
* SQLite
* REST APIs

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

## AI Features

* Resume Parsing
* Question Generation
* Answer Evaluation
* Skill Gap Analysis

---

# Future Enhancements

* Gemini AI Integration
* LinkedIn Analysis
* Company Recommendation Engine
* Mock Video Interviews
* Voice-Based Interview Evaluation
* Real-Time Recruiter Dashboard

---

Version: 1.0.0
