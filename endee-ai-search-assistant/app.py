# app.py
from endee import Endee
import streamlit as st
import os
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
ENDEE_API_KEY = os.getenv("ENDEE_API_KEY")

# Initialize Endee client
client = Endee(token=ENDEE_API_KEY)

# Streamlit interface
st.title("Endee AI Search Assistant")
query = st.text_input("Enter your query:")

if query:
    # Perform a semantic search
    results = client.search(query=query, top_k=5)  # top_k is number of results
    st.write("Results:")
    for i, res in enumerate(results):
        st.write(f"{i+1}. {res['text']}")
