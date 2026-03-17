import streamlit as st

st.title("🤖 Endee AI Search Assistant")

# Input
query = st.text_input("Ask a question:")

# Button
if st.button("Submit"):
    if not query:
        st.warning("Please enter a question")
    else:
        st.write("### Answer:")

        # Simple demo AI logic
        if "ai" in query.lower():
            st.write("Artificial Intelligence is the simulation of human intelligence by machines.")

        elif "machine learning" in query.lower():
            st.write("Machine Learning is a subset of AI that allows systems to learn from data.")

        elif "python" in query.lower():
            st.write("Python is a programming language used for web development, AI, and data science.")

        else:
            st.write("This is a demo response. The system can be extended with real AI using APIs.")
