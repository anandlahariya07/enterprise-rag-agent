from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
import os
import time

from dotenv import load_dotenv
load_dotenv()

def get_retriever(metadata_filter=None):
    start = time.time()
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Qdrant.from_existing_collection(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name="notion_docs",
        embedding=embeddings,
    )

    search_kwargs = {"k": 2}

    if metadata_filter:
        search_kwargs["filter"] = metadata_filter
    
    print(f"Retriever setup time: {time.time() - start:.2f}s")

    return db.as_retriever(search_kwargs=search_kwargs)
