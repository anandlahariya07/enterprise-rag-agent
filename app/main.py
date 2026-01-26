from fastapi import FastAPI
from app.rag.retriever import get_retriever
from app.agents.answer_agent import answer_question

app = FastAPI(title="Enterprise RAG Agent")

retriever = get_retriever()

@app.post("/query")
def query(data: dict):
    question = data["question"]
    docs = retriever.invoke(question)
    context = "\n".join([d.page_content for d in docs])
    answer = answer_question(context, question)

    return {
        "answer": answer
    }
