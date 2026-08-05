import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_questions(interview_type, difficulty, num_questions):

    prompt = f"""
Generate {num_questions} {difficulty} level interview questions
for a {interview_type} interview.

Return ONLY the questions.

Number them.

Example:

1. Tell me about yourself.

2. What are your strengths?

3. Why should we hire you?
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        questions = response.text.split("\n")

        questions = [q for q in questions if q.strip()]

        return questions

    except Exception:

        print("Gemini is unavailable. Using default interview questions.")

        return [
            "1. Tell me about yourself.",
            "2. What are your strengths?",
            "3. Why should we hire you?",
            "4. Explain your MCA project.",
            "5. Where do you see yourself in 5 years?"
        ][:num_questions]