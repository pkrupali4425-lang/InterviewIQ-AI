import os
from dotenv import load_dotenv

from google import genai

from backend.loader import load_pdf
from backend.chunker import split_documents
from backend.vector_db import create_vector_store

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_pdf(pdf_path, question):

    # Load PDF
    documents = load_pdf(pdf_path)

    # Split into chunks
    chunks = split_documents(documents)

    # Create Vector Database
    vectordb = create_vector_store(chunks)

    # Search similar chunks
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
    model="gemini-3.6-flash",
    contents=prompt,
)

    return response.text