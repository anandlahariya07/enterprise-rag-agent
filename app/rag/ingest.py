from app.loaders.notion_loader import NotionLoader
from app.ingest.pipeline import IngestionPipeline
from app.loaders.pdf_loader import PDFLoader
from app.loaders.multi_loader import MultiLoader


def run():
    notion_loader = NotionLoader(page_ids = [
        "de654e343ba9823fbe3281b4f0e53ce8",
        "d1d54e343ba983928e05817153426a33",
        "52254e343ba98363a9cc0100654700d2",
        "13e54e343ba983489e8e016fe3b19940"
    ])

    pdf_loader = PDFLoader(folder_path="data")

    mulit_loader = MultiLoader([
        notion_loader,
        pdf_loader
    ])

    pipeline = IngestionPipeline(loader=mulit_loader)
    pipeline.run()


if __name__ == "__main__":
    run()