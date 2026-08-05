# InterviewIQ-AI

AI-powered Interview Preparation Assistant using Streamlit, Google Gemini, LangChain, FAISS, and Hugging Face.

## Features

- 📄 Interview Chat (RAG-based PDF Chat)
- 📑 Resume Analyzer
- 💼 Job Description Matcher
- 🎤 Mock Interview

## Installation

Clone the repository:

```bash
git clone https://github.com/pkrupali4425-lang/InterviewIQ-AI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## API Configuration

This project uses the **Google Gemini API**.

To use the AI features, create your own Gemini API key from Google AI Studio.

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own API key.

> **Note:** The API key is **not included** in this repository for security reasons.

## Run the Project

```bash
streamlit run app.py
```

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- LangChain
- FAISS
- Hugging Face Embeddings

## Author

**Krupali Prajapati**