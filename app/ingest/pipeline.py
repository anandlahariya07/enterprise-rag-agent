from app.ingest.chunker import DocumentChunker
from app.ingest.embedder import DocumentEmbedder
from app.ingest.store import VectorStore

class IngestionPipeline:
    def __init__(self, loader):
        self.loader = loader
        self.chunker = DocumentChunker()
        self.embedder = DocumentEmbedder()

    def run(self):
        docs = self.loader.load()
        chunks = self.chunker.chunk(docs)

        store = VectorStore(self.embedder.get())
        store.store(chunks)
