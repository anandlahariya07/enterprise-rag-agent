=> Enterprise RAG System (Notion + HuggingFace + Qdrant)

A production-style Retrieval-Augmented Generation (RAG) system that ingests documents dynamically from Notion, generates embeddings using HuggingFace sentence transformers, stores them in Qdrant Cloud, and answers user queries via a FastAPI service.

This project is designed as a real-world RAG architecture, not a toy demo.

=>  What This System Does

Fetches documents dynamically from Notion

Converts text into semantic embeddings using HuggingFace

Stores embeddings in Qdrant (Vector Database)

Retrieves relevant document chunks for a user query

Returns answers grounded in the source documents

=> Why This Is a Real RAG System

Unlike simple demos:

No hardcoded files

No fake embeddings

No local-only vector storage

Clean separation between ingestion and querying

Cloud-ready architecture

This mirrors how enterprise knowledge assistants are built.

=> High-Level Architecture
Notion (Data Source)
        ↓
Ingestion Pipeline
  - Fetch documents
  - Chunk text
  - Generate embeddings
        ↓
Qdrant Cloud (Vector Store)
        ↓
Retriever
        ↓
FastAPI (/query endpoint)
        ↓
Answer Generator

=> Project Structure
app/
├── api/
│   └── main.py          # FastAPI entry point
│
├── rag/
│   ├── ingest.py        # Notion ingestion + embedding + storage
│   ├── retriever.py     # Vector search logic
│
├── agents/
│   └── answer_agent.py  # Answer generation logic
│
├── loaders/
│   └── notion_loader.py # Fetch documents from Notion
│
├── config/
│   └── settings.py      # Environment variable handling
│
requirements.txt
.env.example
README.md

🔧 Tech Stack
Component	Technology
API	FastAPI
Embeddings	HuggingFace (sentence-transformers)
Vector DB	Qdrant Cloud
Data Source	Notion API
RAG Framework	LangChain (light usage)
Language	Python
=> Environment Variables

Create a .env file (do not commit it):

NOTION_API_KEY=your_notion_token
QDRANT_URL=https://your-cluster.qdrant.tech
QDRANT_API_KEY=your_qdrant_api_key


Use .env.example as reference.

=> Ingestion Flow (One-Time or Periodic)

Run ingestion to fetch and index documents:

python app/rag/ingest.py


What happens:

Documents are fetched from Notion

Text is chunked

Embeddings are generated

Vectors are stored in Qdrant

Ingestion is separate from querying by design.

🔍 Querying the System

Start the API:

uvicorn app.api.main:app --reload


Query endpoint:

POST /query


Example payload:

{
  "question": "What is this system about?"
}


The response is generated using retrieved document context.

🧩 Why Ingestion Is Separate from Querying

Documents change infrequently

Queries happen frequently

Re-embedding on every query is inefficient

Enables scheduled or background ingestion jobs

This is standard practice in production RAG systems.

🔁 Extensibility (Next Steps)

This system is intentionally modular and can be extended to:

Multiple ingestion sources (PDFs, Confluence, ServiceNow)

Hybrid search (keyword + vector)

Real LLM answer generation (OpenAI / Azure OpenAI)

Re-ranking models

Caching

Authentication & rate limiting

🛡️ Security Notes

API keys are never committed

.env is ignored via .gitignore

Designed for safe deployment to cloud platforms

📌 Status

✅ Dynamic ingestion
✅ Real embeddings
✅ Cloud vector DB
✅ Working API
🚧 Multi-source ingestion (in progress)

✨ Author Notes

This project is built as a learning-to-production journey, focusing on:

Correct architecture

Real-world constraints

Clean evolution