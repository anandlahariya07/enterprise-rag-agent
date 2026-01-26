# Enterprise RAG Assistant

This project demonstrates a basic Retrieval-Augmented Generation (RAG)
system that allows users to query internal documents through a REST API.

## Architecture Overview
- Document ingestion and indexing using FAISS
- Vector-based retrieval for relevant context
- Answer generation via a simple agent abstraction
- FastAPI used to expose the system as an API

## Workflow
1. Documents are ingested and indexed into a FAISS vector store
2. A user sends a question to the `/query` endpoint
3. Relevant context is retrieved using vector similarity search
4. An answer is generated from the retrieved context

## Tech Stack
- Python
- FastAPI
- LangChain
- FAISS (vector store)

## Notes on LLM & Embeddings
Due to API quota limitations, local embeddings and a stubbed answer agent
are used in this implementation. In a production setup, this can be
replaced with OpenAI / Azure OpenAI services without changing the
overall architecture.

## Production Mapping (Azure)
- Azure OpenAI → LLM & embeddings
- Azure AI Search → Vector store
- Azure App Service → API hosting

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Start the API server:
    uvicorn app.main:app --reload

3. Open Swagger UI in browser:
    http://127.0.0.1:8000/docs

4. Send a request to the /query endpoint with a question.