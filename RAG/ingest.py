from config import EMBED_MODEL_ID, CHROMA_DIR

from langchain_docling import DoclingLoader
from langchain_docling.loader import ExportType
from docling.chunking import HybridChunker
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

FILE_PATH = r"C:\Users\Archi\Desktop\student_assistant\data\BTech_FAQs.pdf"

def build_index():
    loader = DoclingLoader(
        file_path=FILE_PATH,
        export_type=ExportType.DOC_CHUNKS,
        chunker=HybridChunker(tokenizer=EMBED_MODEL_ID),
    )
    docs = loader.load()
    docs = filter_complex_metadata(docs)

    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL_ID)

    Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
    print(f"Indexed {len(docs)} chunks → {CHROMA_DIR}")

if __name__ == "__main__":
    build_index()