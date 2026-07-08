# app/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chain import build_rag_chain

app = FastAPI()
rag_chain = build_rag_chain()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(payload: Question):
    result = rag_chain.invoke(payload.question)
    return result  # {"answer": "...", "sources": [{"source": ..., "page": ...}]}