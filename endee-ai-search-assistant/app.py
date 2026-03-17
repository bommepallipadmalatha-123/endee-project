# app.py
import streamlit as st
import os
from dotenv import load_dotenv
from endee import Endee

# Load environment variables
load_dotenv()

# Get API key
ENDEE_API_KEY = os.getenv("ENDEE_API_KEY")

# Initialize Endee
client = Endee(token=ENDEE_API_KEY)

# UI
st.title("Endee AI Search Assistant")

query = st.text_input("Enter your query:")

if query:
    try:
        # Correct method (generic safe call)
        response = client.query(query)

        st.write("Response:")
        st.write(response)

    except Exception as e:
        st.error(f"Error: {e}")
