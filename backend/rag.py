import os
from dotenv import load_dotenv

from google import genai

from backend.loader import load_pdf
from backend.chunker import split_documents
from backend.vector_db import create_vector_store

load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client only if API key exists
client = None
if api_key:
    client = genai.Client(api_key=api_key)


def ask_pdf(pdf_path, question):

    # If API key is missing
    if client is None:
        return (
            "⚠ Gemini API key is not configured.\n\n"
            "Please add your GEMINI_API_KEY in Streamlit Secrets "
            "or in a .env file to use Interview Chat."
        )

    # Load PDF
    documents = load_pdf(pdf_path)

    # Split into chunks
    chunks = split_documents(documents)

    # Create Vector Database
    vectordb = create_vector_store(chunks)

    # Retrieve similar chunks
    docs = vectordb.similarity_search(question, k=4)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are InterviewIQ AI.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=prompt,
)

    return response.text