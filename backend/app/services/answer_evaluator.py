import re


def evaluate_answer(answer: str):
    """
    Basic answer evaluation logic.
    Returns score, feedback and confidence level.
    """

    if not answer:
        return {
            "score": 0,
            "feedback": "No answer provided.",
            "confidence": "Low"
        }

    word_count = len(answer.split())

    # Technical keywords
    keywords = [
        "python",
        "react",
        "sql",
        "api",
        "machine learning",
        "database",
        "algorithm",
        "project",
        "backend",
        "frontend"
    ]

    keyword_matches = sum(
        1
        for keyword in keywords
        if keyword.lower() in answer.lower()
    )

    score = min(
        (word_count * 0.5) +
        (keyword_matches * 5),
        100
    )

    # Confidence Detection
    confidence_words = [
        "implemented",
        "developed",
        "built",
        "created",
        "designed",
        "optimized",
        "deployed"
    ]

    confidence_score = sum(
        1
        for word in confidence_words
        if word.lower() in answer.lower()
    )

    if confidence_score >= 3:
        confidence = "High"
    elif confidence_score >= 1:
        confidence = "Medium"
    else:
        confidence = "Low"

    # Feedback

    if score >= 80:
        feedback = (
            "Strong answer with good technical depth."
        )

    elif score >= 60:
        feedback = (
            "Good answer but could include more technical details."
        )

    elif score >= 40:
        feedback = (
            "Average answer. Try explaining your approach clearly."
        )

    else:
        feedback = (
            "Weak answer. Add technical concepts and examples."
        )

    return {
        "score": round(score, 2),
        "feedback": feedback,
        "confidence": confidence,
        "word_count": word_count,
        "keyword_matches": keyword_matches
    }