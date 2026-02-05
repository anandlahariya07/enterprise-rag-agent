from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
import os

from dotenv import load_dotenv
load_dotenv()

print("QDRANT URL:", os.getenv("QDRANT_URL"))

def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    db = Qdrant.from_existing_collection(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name="notion_docs",
        embedding=embeddings,
    )
    return db.as_retriever(search_kwargs={"k": 2})
