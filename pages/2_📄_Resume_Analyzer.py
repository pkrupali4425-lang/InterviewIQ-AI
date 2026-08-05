import os
import streamlit as st

from backend.resume_analyzer import analyze_resume

st.set_page_config(page_title="Resume Analyzer")

st.title("📄 Resume Analyzer")

uploaded = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded:

    os.makedirs("uploads", exist_ok=True)

    path = os.path.join(
        "uploads",
        uploaded.name
    )

    with open(path, "wb") as f:
        f.write(uploaded.getbuffer())

    with st.spinner("Analyzing Resume..."):

        result = analyze_resume(path)

    st.success("Analysis Completed")

    st.subheader("Candidate Details")

    st.write("👤 Name:", result["name"])
    st.write("📧 Email:", result["email"])
    st.write("📱 Phone:", result["phone"])

    st.subheader("ATS Score")

    st.progress(result["score"] / 100)

    st.write(f"### {result['score']} / 100")

    st.subheader("Skills")

    if result["skills"]:
        for skill in result["skills"]:
            st.success(skill)
    else:
        st.warning("No skills found")

    st.subheader("Suggestions")

    for s in result["suggestions"]:
        st.info(s)