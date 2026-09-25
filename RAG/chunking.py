import os
from pathlib import Path
from dotenv import load_dotenv

from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from langchain_core.documents import Document
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ---------------------------------------------------------------
# 1. Load environment variables from student_assistant/.env
# ---------------------------------------------------------------
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError(f"GROQ_API_KEY not found. Checked: {env_path}")

# ---------------------------------------------------------------
# 2. Convert PDF -> Docling document
# ---------------------------------------------------------------
PDF_PATH = r"C:\Users\Archi\Desktop\student_assistant\data\BTech_FAQs.pdf"  # adjust path as needed

converter = DocumentConverter()
result = converter.convert(PDF_PATH)
dl_doc = result.document

# ---------------------------------------------------------------
# 3. Chunk the Docling document
# ---------------------------------------------------------------
chunker = HybridChunker()
chunk_iter = chunker.chunk(dl_doc)

docs = []
for chunk in chunk_iter:
    text = chunker.contextualize(chunk)  # includes headings for better retrieval
    docs.append(
        Document(
            page_content=text,
            metadata={"dl_meta": chunk.meta.export_json_dict()},
        )
    )

print(f"Created {len(docs)} chunks")

# ---------------------------------------------------------------
# 4. Strip complex/nested metadata Chroma can't store
# ---------------------------------------------------------------
docs = filter_complex_metadata(docs)

# ---------------------------------------------------------------
# 5. Embed + store in Chroma
# ---------------------------------------------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db",
)

print("Vectorstore built and persisted to ./chroma_db")