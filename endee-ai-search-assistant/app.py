import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import openai

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Title
st.title("Endee AI Knowledge Assistant")

# Upload files
uploaded_files = st.file_uploader("Upload PDF or TXT", accept_multiple_files=True)

documents = []

# Read uploaded files
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

# Form (Enter + Button works)
with st.form("form"):
    query = st.text_input("Ask a question")
    submit = st.form_submit_button("Submit")

# Process
if submit:
    if not documents:
        st.warning("Please upload a file first")

    elif not query:
        st.warning("Please enter a question")

    else:
        # Simple search
        relevant = []
        for doc in documents:
            if query.lower() in doc.lower():
                relevant.append(doc)

        if not relevant:
            relevant = documents[:2]

        context = " ".join(relevant)[:3000]

        # AI response
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"Answer using this context:\n{context}\n\nQuestion: {query}"
                    }
                ]
            )

            st.write("Answer:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(e)
