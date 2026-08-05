import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="InterviewIQ AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""

<style>

.main{
    background-color:#0E1117;
}

h1{
    color:#4FC3F7;
    text-align:center;
}

h2{
    color:white;
}

div[data-testid="metric-container"]{
    background:#1E1E1E;
    padding:20px;
    border-radius:15px;
    border:1px solid #2E2E2E;
}

div[data-testid="metric-container"]:hover{
    border:1px solid #4FC3F7;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    background:#4FC3F7;
    color:black;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🤖 InterviewIQ AI")
st.sidebar.markdown("---")

st.sidebar.success("AI Powered Interview Preparation")

st.sidebar.write("Navigate using the pages below.")

st.sidebar.markdown("---")

st.sidebar.info(
"""
Modules

• Interview Chat

• Resume Analyzer

• JD Matcher

• Mock Interview

• Image Solver

• Analytics
"""
)

# -------------------------------
# Main Heading
# -------------------------------
st.title("🤖 InterviewIQ AI")

st.subheader("Prepare Smarter • Interview Better • Get Hired")
st.markdown("""
### 🎯 Your Personal AI Interview Preparation Assistant

Prepare for Technical, HR and Aptitude interviews using AI.

Upload documents • Analyze Resume • Practice Interviews • Improve Skills
""")
st.markdown("---")

# -------------------------------
# Statistics
# -------------------------------
st.header("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Documents Uploaded",
        value="0"
    )

with col2:
    st.metric(
        label="Questions Asked",
        value="0"
    )

with col3:
    st.metric(
        label="Mock Interviews",
        value="0"
    )

st.markdown("---")

# -------------------------------
# Features
# -------------------------------
st.header("🚀 AI Features")

left, right = st.columns(2)

with left:

    st.success("💬 AI Interview Chat")

    st.success("📄 Resume Analyzer")

    st.success("💼 Job Description Matcher")

    st.success("🎤 Mock Interview")

with right:

    st.success("🖼 Image Question Solver")

    st.success("🎙 Speech To Text")

    st.success("🔊 Text To Speech")

    st.success("📊 Analytics Dashboard")

st.markdown("---")

# -------------------------------
# Quick Start
# -------------------------------
st.header("⚡ Quick Start")

col1,col2,col3=st.columns(3)

with col1:
    st.button("📄 Upload Documents")

with col2:
    st.button("💬 Start Chat")

with col3:
    st.button("🎤 Mock Interview")
"""
1. Upload Interview Notes

2. Ask Questions

3. Practice Mock Interviews

4. Improve Your Resume

5. Track Your Progress
"""
