from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings

loader = TextLoader("data/documents/sample_policy.txt")
docs = loader.load()

# Local fake embeddings (no API needed)
embeddings = FakeEmbeddings(size=384)

db = FAISS.from_documents(docs, embeddings)
db.save_local("faiss_index")

print("Documents indexed (using local embeddings)")
