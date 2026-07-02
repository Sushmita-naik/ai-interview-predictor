import re
import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF resume
    """

    text = ""

    try:
        document = fitz.open(pdf_path)

        for page in document:
            text += page.get_text()

        document.close()

    except Exception as e:
        print("PDF Parsing Error:", e)

    return text


def extract_email(text):

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    emails = re.findall(
        email_pattern,
        text
    )

    return emails[0] if emails else None


def extract_phone(text):

    phone_pattern = r"\+?\d[\d\s\-]{8,15}"

    phones = re.findall(
        phone_pattern,
        text
    )

    return phones[0] if phones else None


def extract_skills(text):

    skill_keywords = [
        "Python",
        "Java",
        "C++",
        "React",
        "Node.js",
        "FastAPI",
        "Django",
        "Flask",
        "SQL",
        "MongoDB",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "Docker",
        "AWS",
        "Git",
        "HTML",
        "CSS",
        "JavaScript"
    ]

    found_skills = []

    for skill in skill_keywords:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))


def extract_projects(text):

    project_keywords = [
        "project",
        "developed",
        "built",
        "implemented",
        "created"
    ]

    projects = []

    lines = text.split("\n")

    for line in lines:

        for keyword in project_keywords:

            if keyword.lower() in line.lower():

                if len(line.strip()) > 10:
                    projects.append(
                        line.strip()
                    )

    return projects[:10]


def parse_resume(pdf_path):

    text = extract_text_from_pdf(
        pdf_path
    )

    parsed_data = {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "projects": extract_projects(text),
        "resume_text": text
    }

    return parsed_data