import os
from pypdf import PdfReader
from langchain.schema import Document


class PDFLoader:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def load(self):
        documents = []

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".pdf"):
                file_path = os.path.join(self.folder_path, filename)

                reader = PdfReader(file_path)

                for page_number, page in enumerate(reader.pages):
                    text = page.extract_text()

                    if text:
                        documents.append(
                            Document(
                                page_content=text,
                                metadata={
                                    "source": filename,
                                    "page": page_number + 1,
                                    "type": "pdf"
                                }
                            )
                        )

        return documents
