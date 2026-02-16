from fastapi import FastAPI
from app.agents.answer_agent import answer_question
import time
from app.rag.retriever import get_retriever

retriever = get_retriever()
app = FastAPI(title="Enterprise RAG Agent")

@app.post("/query")
def query(data: dict):
    start_time = time.time()

    question = data["question"]
    session_id = data["session_id"]
    answer = answer_question(session_id, question, retriever=retriever)

    total_time = time.time() - start_time
    print(f"TOTAL API TIME: {total_time:.2f}s")

    return {
        "answer": answer,
        "response_time_seconds": round(total_time, 2)
    }
