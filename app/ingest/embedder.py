from langchain_community.embeddings import HuggingFaceEmbeddings

class DocumentEmbedder:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/all-MiniLM-L6-v2"
        )

    def get(self):
        return self.embeddings