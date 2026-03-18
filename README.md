🚀 Endee AI Search Assistant

Live Demo

An AI-powered Search Assistant built using the Endee Vector Database, designed to perform intelligent semantic search and retrieve relevant information efficiently.

📌 Overview

Endee AI Search Assistant is a smart application that leverages vector embeddings and semantic search to provide accurate and context-aware results.

Unlike traditional keyword-based search systems, this assistant understands the meaning behind queries, delivering more relevant and precise results from your datasets.

🎯 Features

🔍 Semantic Search (AI-based) – Understands user intent, not just keywords

⚡ Fast Retrieval – Powered by Endee Vector Database for efficient searches

🧠 Context-aware Results – Maintains query context for better answers

📂 Custom Dataset Support – Easily integrate your own data for search

🌐 User-friendly Interface – Built with Streamlit for simplicity and speed

🔗 Seamless Integration – Works directly with Endee Vector DB and OpenAI embeddings

🛠️ Tech Stack

Python – Core application language

Endee Vector Database – Stores embeddings and performs fast semantic searches

Streamlit – Frontend interface (CLI support optional)

OpenAI Embedding Models – Generates semantic embeddings from text

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/bommepallipadmalatha-123/endee-ai-search-assistant.git
cd endee-ai-search-assistant

Install dependencies

pip install -r requirements.txt

Set OpenAI API key

export OPENAI_API_KEY="your_openai_api_key"   # Linux / Mac
setx OPENAI_API_KEY "your_openai_api_key"     # Windows

Run the app

streamlit run app.py

Access in Browser

Open your browser and go to: http://localhost:8501

Or use the Live Streamlit Demo

🗂️ Usage

Upload your dataset (text files, CSV, JSON, etc.)

Generate embeddings via OpenAI models

Query your dataset using natural language questions

Receive context-aware semantic search results instantly

🔧 Folder Structure
endee-ai-search-assistant/
│
├─ app.py              # Main Streamlit application
├─ requirements.txt    # Python dependencies
├─ README.md           # Project documentation
├─ data/               # Custom dataset storage
├─ utils/              # Helper functions (embedding, search)
└─ config/             # Configuration files
💡 Future Enhancements

Multi-modal support (images, audio, video)

Real-time chat interface for semantic QA

Advanced ranking and filtering options

User authentication for secure dataset access

📞 Contact

Created by Padmalatha Bommepalli

GitHub: bommepallipadmalatha-123
