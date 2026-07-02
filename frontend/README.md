# AI Interview Predictor

## Overview

AI Interview Predictor is a machine learning based web application that analyzes a candidate's profile and predicts placement readiness, interview performance, and salary potential.

The system uses resume analysis, skill extraction, interview evaluation, and machine learning models to generate personalized insights and career recommendations.

---

## Features

* User Registration and Login
* Resume Upload (PDF)
* Resume Analysis
* Skill Extraction
* Placement Probability Prediction
* Salary Prediction
* AI-Based Interview Questions
* Interview Evaluation
* Missing Skill Detection
* Personalized Learning Roadmap
* Recruiter-Style Report Generation

---

## Technology Stack

### Frontend

* React.js
* React Router
* CSS

### Backend

* FastAPI
* Python

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

### Database

* SQLite (Initial Version)

---

## Project Structure

frontend/

* React Application

backend/

* FastAPI APIs

ml/

* Datasets
* Training Scripts
* Trained Models
* Experiments Notebook

---

## Machine Learning Models

### Placement Model

Predicts the probability of a candidate getting placed.

### Salary Model

Predicts the expected salary range based on skills, projects, and academic profile.

### Skill Recommendation Engine

Identifies missing skills and recommends technologies to learn.

---

## Workflow

1. User uploads resume.
2. Resume is parsed and analyzed.
3. Skills and projects are extracted.
4. Placement probability is predicted.
5. Salary range is estimated.
6. AI interview is conducted.
7. Final report is generated.

---

## Future Enhancements

* GitHub Profile Analysis
* LinkedIn Profile Analysis
* Video Interview Analysis
* Voice Confidence Detection
* Company Specific Interview Preparation
* Real-Time AI Recruiter

---

## Installation

### Frontend

npm install

npm run dev

### Backend

pip install -r requirements.txt

uvicorn main:app --reload

---

## Author

Developed as a real-world AI and Machine Learning project for interview preparation and placement prediction.