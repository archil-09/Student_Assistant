from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent          # RAG/
ROOT_DIR = BASE_DIR.parent                            # student_assistant/

load_dotenv(dotenv_path=ROOT_DIR / ".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError(f"GROQ_API_KEY not found. Checked: {ROOT_DIR / '.env'}")

EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
CHROMA_DIR = str(BASE_DIR / "chroma_db")