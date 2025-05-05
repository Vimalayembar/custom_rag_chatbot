from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from utils import extract_text_from_pdf  # Import the PDF extraction function

app = FastAPI()

# Load Hugging Face question-answering pipeline
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Request model for POST /ask
class Question(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Custom RAG Chatbot API is running with Hugging Face and PDF support!"}

@app.post("/ask")
async def ask_question(question: Question):
    try:
        # Load context dynamically from a real uploaded PDF
        context = extract_text_from_pdf("sample.pdf")  # Make sure this file exists in your project

        result = qa_model({
            "question": question.query,
            "context": context
        })

        return {"answer": result["answer"]}
    except Exception as e:
        return {"error": str(e)}
