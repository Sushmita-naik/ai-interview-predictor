import random


def generate_interview_questions(
    skills,
    projects=None
):
    """
    Generate personalized interview questions
    based on skills and projects.
    """

    questions = []

    skill_questions = {
        "Python": [
            "What are Python decorators?",
            "Explain list comprehension in Python.",
            "What is the difference between a list and a tuple?"
        ],

        "React": [
            "What are React hooks?",
            "Explain useState and useEffect.",
            "How does React Virtual DOM work?"
        ],

        "SQL": [
            "What is a JOIN?",
            "Difference between WHERE and HAVING?",
            "Explain normalization."
        ],

        "Machine Learning": [
            "What is overfitting?",
            "Difference between supervised and unsupervised learning?",
            "Explain the bias-variance tradeoff."
        ],

        "FastAPI": [
            "Why use FastAPI?",
            "What are Pydantic models?",
            "How do you create API routes?"
        ],

        "Docker": [
            "What is Docker?",
            "Difference between Docker image and container?",
            "What is Docker Compose?"
        ],

        "AWS": [
            "What is EC2?",
            "What is S3?",
            "Explain IAM."
        ]
    }

    for skill in skills:

        if skill in skill_questions:

            selected = random.sample(
                skill_questions[skill],
                min(
                    2,
                    len(skill_questions[skill])
                )
            )

            questions.extend(selected)

        else:

            questions.append(
                f"Explain your experience with {skill}."
            )

    if projects:

        for project in projects:

            questions.extend([
                f"Explain the architecture of {project}.",
                f"What challenges did you face while building {project}?",
                f"What technologies did you use in {project}?",
                f"If you rebuild {project}, what would you improve?"
            ])

    return questions