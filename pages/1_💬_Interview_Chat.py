import os
import streamlit as st

from backend.rag import ask_pdf

st.set_page_config(page_title="Interview Chat")

st.title("📄 InterviewIQ AI")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF Uploaded Successfully")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        with st.spinner("Thinking..."):

            answer = ask_pdf(
                pdf_path,
                question
            )

        st.success(answer)