from langchain_community.embeddings import HuggingFaceEmbeddings
from app.utils.notion_loader import fetch_notion_pages
from langchain_core.documents import Document
import os
from langchain_qdrant import Qdrant

from dotenv import load_dotenv
load_dotenv()

page_ids = [
    "de654e343ba9823fbe3281b4f0e53ce8",
    "d1d54e343ba983928e05817153426a33",
    "52254e343ba98363a9cc0100654700d2",
    "13e54e343ba983489e8e016fe3b19940"
]

texts = fetch_notion_pages(page_ids)
docs = [Document(page_content=t) for t in texts]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Qdrant.from_documents(
    docs,
    embedding=embeddings,
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    collection_name="notion_docs",
)
print("Documents indexed (using local embeddings)")
