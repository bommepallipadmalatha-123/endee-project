import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import openai

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Endee AI Knowledge Assistant")

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

# Ask question
query = st.text_input("Ask a question")

if query and documents:

    relevant = []
    for doc in documents:
        if query.lower() in doc.lower():
            relevant.append(doc)

    if not relevant:
        relevant = documents[:2]

    context = " ".join(relevant)[:3000]

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Answer using this context:\n{context}\n\nQuestion: {query}"}
        ]
    )

    st.write("### Answer:")
    st.write(response.choices[0].message.content)
