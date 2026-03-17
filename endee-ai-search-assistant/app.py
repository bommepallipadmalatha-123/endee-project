import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Endee AI Search Assistant")

# Upload files
uploaded_files = st.file_uploader("Upload PDF or TXT", accept_multiple_files=True)

documents = []

# Read files
if uploaded_files:
    for file in uploaded_files:
        if file.name.endswith(".pdf"):
            pdf = PdfReader(file)
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            documents.append(text)

        elif file.name.endswith(".txt"):
            documents.append(file.read().decode("utf-8"))

# Form (fix Enter issue)
with st.form("form"):
    query = st.text_input("Ask a question")
    submit = st.form_submit_button("Submit")

# Generate Answer
if submit:
    if not documents:
        st.warning("Upload file first")
    elif not query:
        st.warning("Enter question")
    else:
        # Simple retrieval
        context = " ".join(documents)[:3000]

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": f"Answer using this context:\n{context}\n\nQuestion: {query}"}
                ]
            )

            answer = response.choices[0].message.content

            st.write("### Answer:")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")
