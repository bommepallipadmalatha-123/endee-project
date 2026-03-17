import streamlit as st
from openai import OpenAI

# ✅ put key inside quotes
client = OpenAI(api_key="sk-proj-xxxxxxxxxxxxxxxx")

st.title("AI Assistant")

query = st.text_input("Ask:")

if st.button("Submit"):
    if query:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": query}]
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.write("Error:", e)
