import os
import streamlit as st

# Import functions from app.py
from app import run_pipeline, answer_question

st.set_page_config(
    page_title="Multimodal RAG System",
    page_icon="📄",
    layout="wide"
)

st.title(" Multimodal RAG System")
st.write("Upload a PDF, process it, and ask questions about the document.")

# -----------------------------
# Session State Initialization
# -----------------------------
if "document_processed" not in st.session_state:
    st.session_state.document_processed = False

# -----------------------------
# PDF Upload Section
# -----------------------------
st.header("1️⃣ Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Process Document"):

        # Save uploaded file temporarily
        temp_dir = "temp_uploads"
        os.makedirs(temp_dir, exist_ok=True)

        pdf_path = os.path.join(
            temp_dir,
            uploaded_file.name
        )

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Running RAG Pipeline..."):

            try:
                run_pipeline(pdf_path)

                st.session_state.document_processed = True

                st.success(
                    "✅ Document processed successfully!"
                )

            except Exception as e:

                st.error(
                    f"Pipeline failed:\n{e}"
                )

# -----------------------------
# Question Answering Section
# -----------------------------
if st.session_state.document_processed:

    st.header("2️⃣ Ask Questions")

    question = st.text_input(
        "Enter your question:"
    )

    if st.button("Get Answer"):

        if question.strip():

            with st.spinner(
                "Searching relevant information..."
            ):

                try:

                    results = answer_question(
                        question
                    )

                    st.subheader(
                        "Retrieved Context"
                    )

                    if results:

                      result = results[0]
                      st.write(f"**Document:** {result.get('document_name')}")
                      st.write(f"**Page:** {result.get('page_number')}")
                      st.write(f"**Location:** {result.get('location')}")
                      st.write("**Summary:**")
                      st.info(result.get("summary"))    

                    else:

                        st.warning(
                            "No relevant results found."
                        )

                except Exception as e:

                    st.error(
                        f"Failed to answer question:\n{e}"
                    )