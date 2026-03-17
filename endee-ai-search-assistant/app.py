import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Title
st.title("🤖 Endee AI Search Assistant")

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

# Form (Enter + button works)
with st.form("form"):
    query = st.text_input("Ask a question")
    submit = st.form_submit_button("Submit")

# Answer generation (ALWAYS gives output)
if submit:
    if not query:
        st.warning("Please enter a question")

    else:
        # If documents exist → use them
        if documents:
            context = " ".join(documents)[:3000]
            prompt = f"""
You are an AI assistant.

Answer using the context below.
If answer is not in context, still answer generally.

Context:
{context}

Question:
{query}
"""
        else:
            # No documents → general answer
            prompt = query

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            answer = response.choices[0].message.content

            st.write("### ✅ Answer:")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")
