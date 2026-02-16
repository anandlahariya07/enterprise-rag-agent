from langchain_qdrant import Qdrant
import os
from dotenv import load_dotenv

load_dotenv()

class VectorStore:
    def __init__(self, embeddings):
        self.embeddings = embeddings

    def store(self, documents):
        Qdrant.from_documents(
        documents,
        embedding= self.embeddings,
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name="notion_docs",
    )