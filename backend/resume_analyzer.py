import pdfplumber
import re

SKILLS = [
    "python","java","c","c++","sql","mysql","mongodb",
    "power bi","excel","machine learning","deep learning",
    "html","css","javascript","react","node","flask",
    "django","git","github","aws","docker","linux",
    "tensorflow","numpy","pandas","streamlit"
]


def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):
    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return email[0] if email else "Not Found"


def extract_phone(text):

    phone = re.findall(
        r"\+?\d[\d\s-]{8,}\d",
        text
    )

    return phone[0] if phone else "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines[:5]:
        if len(line.split()) <= 4:
            return line

    return "Not Found"


def extract_skills(text):

    found = []

    text = text.lower()

    for skill in SKILLS:

        if skill in text:
            found.append(skill.title())

    return found


def calculate_score(text, skills):

    score = 0

    if extract_name(text) != "Not Found":
        score += 10

    if extract_email(text) != "Not Found":
        score += 10

    if extract_phone(text) != "Not Found":
        score += 10

    score += min(len(skills) * 3, 40)

    if "education" in text.lower():
        score += 15

    if "project" in text.lower():
        score += 15

    return min(score, 100)


def analyze_resume(pdf_path):

    text = extract_text(pdf_path)

    skills = extract_skills(text)

    score = calculate_score(text, skills)

    suggestions = []

    if "github" not in text.lower():
        suggestions.append("Add GitHub profile")

    if "internship" not in text.lower():
        suggestions.append("Mention Internship Experience")

    if "certification" not in text.lower():
        suggestions.append("Add Certifications")

    if len(skills) < 5:
        suggestions.append("Mention more technical skills")

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": skills,
        "score": score,
        "suggestions": suggestions
    }