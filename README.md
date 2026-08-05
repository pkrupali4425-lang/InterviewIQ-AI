# InterviewIQ-AI
AI-powered Interview Preparation Assistant using LLM and RAG
## Deployment Instructions


1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

4. Run the application:

```bash
streamlit run app.py
```


## API Configuration

This project uses the Google Gemini API for AI-powered features such as:

- AI Interview Chat
- Resume Analyzer
- Job Description Matcher
- Mock Interview

To enable these features, create your own Google Gemini API key and add it as an environment variable.

### Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own Google Gemini API key.

> **Note:** For security reasons, the API key is **not included** in this repository. Users must provide their own API key to use the AI features.