import streamlit as st
from sentence_transformers import SentenceTransformer
import endee

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize DB
db = endee.Client()

st.title("AI Search Assistant using Endee")

# Load sample data
with open("data/sample.txt", "r") as file:
    data = file.readlines()

# Store data button
if st.button("Store Data"):
    for line in data:
        embedding = model.encode(line).tolist()
        db.insert({"text": line, "vector": embedding})
    st.success("Data stored successfully!")

# Query
query = st.text_input("Ask a question")

if st.button("Search"):
    query_embedding = model.encode(query).tolist()
    results = db.search(query_embedding, top_k=3)

    st.write("Results:")
    for r in results:
        st.write(r["text"])