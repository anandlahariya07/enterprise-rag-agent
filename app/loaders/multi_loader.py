from typing import List
from langchain.schema import Document


class MultiLoader:
    def __init__(self, loaders: list):
        self.loaders = loaders

    def load(self) -> List[Document]:
        all_documents = []

        for loader in self.loaders:
            documents = loader.load()
            all_documents.extend(documents)

        return all_documents
