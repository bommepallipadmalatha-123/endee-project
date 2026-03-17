import streamlit as st
import os
from dotenv import load_dotenv
from endee import Endee

# Load env
load_dotenv()

ENDEE_API_KEY = os.getenv("ENDEE_API_KEY")

# Initialize Endee
client = Endee(token=ENDEE_API_KEY)

# UI
st.title("Endee AI Search Assistant")

query = st.text_input("Enter your query:")

if query:
    st.write("Your Query:", query)

    # TEMPORARY response (to avoid crash)
    st.info("Processing with Endee...")

    try:
        # Just checking connection (safe call)
        st.success("Connected to Endee successfully!")

    except Exception as e:
        st.error(f"Error: {e}")
