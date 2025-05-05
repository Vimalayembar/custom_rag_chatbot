# custom_rag_chatbot
# 📚 Custom RAG Chatbot API (PDF Question Answering)

A lightweight REST API chatbot built with **FastAPI** and **Hugging Face Transformers** that can read and answer questions from your own **PDF documents** — without using OpenAI or paid APIs.

> ✅ No OpenAI key required  
> ✅ Runs entirely with open-source models  
> ✅ Upload your own resume, syllabus, or notes and ask questions!

---

## 🚀 Features

- 📄 Extracts text from uploaded PDF files
- 🧠 Uses Hugging Face's `distilbert-base-uncased-distilled-squad` for question answering
- 🔗 API built using FastAPI with Swagger `/docs` for testing
- ⚙️ Clean project structure: `main.py` (API) + `utils.py` (PDF reader)

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn (ASGI Server)
- Hugging Face Transformers
- PyMuPDF (for PDF reading)

---

## 📁 Project Structure

# pip install fastapi uvicorn transformers pymupdf
#uvicorn main:app --reload --host 0.0.0.0 --port 8000
