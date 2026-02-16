import os
from dotenv import load_dotenv
from notion_client import Client
from langchain.schema import Document

load_dotenv()

class NotionLoader:
    def __init__(self, page_ids: list[str]):
        self.page_ids = page_ids
        self.client = Client(auth=os.getenv("NOTION_TOKEN"))

    def load(self) -> list[Document]:
        documents = []

        for page_id in self.page_ids:
            blocks = self.client.blocks.children.list(block_id=page_id)

            text = ""

            for block in blocks["results"]:
                if "paragraph" in block:
                    rich_text = block["paragraph"]["rich_text"]
                    if rich_text:
                        text += rich_text[0]["plain_text"] + "\n"

            documents.append(
                Document(
                    page_content=text,
                    metadata={"source": page_id}
                )
            )

        return documents
