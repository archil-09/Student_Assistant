import torch

from langchain_docling import DoclingLoader


FILE_PATH = [r"C:\Users\Archi\Desktop\student_assistant\data\BTech_FAQs.pdf"]  # Docling Technical Report

loader = DoclingLoader(file_path=FILE_PATH)

docs = loader.load()
for d in docs:
    print(d.page_content)