from dotenv import load_dotenv
import os
from notion_client import Client

load_dotenv()
print("TOKEN BEING USED:", os.getenv("NOTION_API_KEY"))

notion = Client(auth=os.getenv("NOTION_TOKEN"))

def fetch_notion_pages(page_ids):
    docs = []

    for page_id in page_ids:
        blocks = notion.blocks.children.list(block_id=page_id)
        text = ""

        for block in blocks["results"]:
            if "paragraph" in block and block["paragraph"]["rich_text"]:
                text += block["paragraph"]["rich_text"][0]["plain_text"] + "\n"

        docs.append(text)

    return docs
