import streamlit as st

from backend.mock_interview import generate_questions
from backend.tts import text_to_speech

st.title("🎤 AI Mock Interview")

interview = st.selectbox(
    "Interview Type",
    ["HR", "Technical", "Aptitude"]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

num = st.slider(
    "Number of Questions",
    1,
    10,
    5
)

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current" not in st.session_state:
    st.session_state.current = 0

if st.button("Start Interview"):

    st.session_state.questions = generate_questions(
        interview,
        difficulty,
        num
    )

    st.session_state.current = 0


if st.session_state.questions:

    st.subheader("Question")

    st.write(
        st.session_state.questions[
            st.session_state.current
        ]
    )
if "audio" not in st.session_state:
    st.session_state.audio = None

if st.button("🔊 Listen Question"):

    st.session_state.audio = text_to_speech(
        st.session_state.questions[
            st.session_state.current
        ]
    )

if st.session_state.audio:
    st.audio(st.session_state.audio)
    

    answer = st.text_area(
        "Your Answer"
    )

    if st.button("Next Question"):

        if st.session_state.current < len(st.session_state.questions)-1:

            st.session_state.current += 1

        else:

            st.success("Interview Completed 🎉")