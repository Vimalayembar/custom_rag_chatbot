# 🤖 Custom RAG Chatbot API (PDF Question Answering)

A lightweight REST API chatbot built with **FastAPI** and **Hugging Face Transformers** that can read and answer questions from your own PDF documents — without using OpenAI or paid APIs.

---

### ✅ Key Features

- 📄 Reads and understands uploaded PDF files
- 🧠 Uses Hugging Face’s `distilbert-base-uncased-distilled-squad` model
- 🔗 Built with FastAPI and tested via `/docs` (Swagger UI)
- 💡 No API key or paid service required — runs 100% locally with open models

---

### 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn (ASGI server)
- Hugging Face Transformers
- PyMuPDF (`fitz`) for PDF parsing

---

### 🗂 Project Structure

custom_rag_chatbot/
├── main.py # FastAPI app logic
├── utils.py # PDF extraction helper
├── sample.pdf # Your uploaded document
├── README.md # This file

yaml
Copy
Edit

---

### 🚀 Getting Started

#### 1. Install Dependencies

```bash
pip install fastapi uvicorn transformers pymupdf
2. Run the Server
bash
Copy
Edit
uvicorn main:app --reload --host 0.0.0.0 --port 8000
📥 Upload Your PDF
Upload a .pdf file (like a resume or article) and rename it as:

Copy
Edit
sample.pdf
📌 Make sure it has text, not just images!

📘 Try It Out
Go to: http://localhost:8000/docs

Use the POST /ask endpoint

Example query:

json
Copy
Edit
{
  "query": "What is this document about?"
}
✅ If successful, you’ll get an answer based on the PDF content.