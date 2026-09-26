from langchain_docling.loader import DoclingLoader

FILE_PATH = r"C:\Users\Archi\Desktop\student_assistant\data\BTech_FAQs.pdf"

loader = DoclingLoader(file_path=FILE_PATH)

# Load all documents
documents = loader.load()

# For large datasets, lazily load documents
for document in loader.lazy_load():
    print(document)

