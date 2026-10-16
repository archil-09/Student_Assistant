
from pathlib import Path

from config import EMBED_MODEL_ID, CHROMA_DIR

from langchain_docling import DoclingLoader
from langchain_docling.loader import ExportType
from docling.chunking import HybridChunker
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

FILE_PATH = r"C:\Users\Archi\Desktop\student_assistant\data\BTech_FAQs.pdf"
mtech_vi = r"C:\Users\Archi\Desktop\student_assistant\data\M.Tech_IV.pdf"


def build_index():
    pdf_paths = [FILE_PATH, mtech_vi]
    all_docs = []

    for pdf_path in pdf_paths:
        loader = DoclingLoader(
            file_path=pdf_path,
            export_type=ExportType.DOC_CHUNKS,
            chunker=HybridChunker(tokenizer=EMBED_MODEL_ID,max_tokens=1000),
        )

        docs = loader.load()

        # Identify the source PDF for each chunk
        for doc in docs:
            doc.metadata["source"] = Path(pdf_path).name

        all_docs.extend(docs)
        print(f"Loaded {len(docs)} chunks from {Path(pdf_path).name}")

    all_docs = filter_complex_metadata(all_docs)

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBED_MODEL_ID
    )

    Chroma.from_documents(
        documents=all_docs,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )

    print(f"Indexed {len(all_docs)} total chunks → {CHROMA_DIR}")


if __name__ == "__main__":
    build_index()