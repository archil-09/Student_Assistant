from docling.document_converter import DocumentConverter

doc = DocumentConverter().convert(r"data\M.Tech_IV.pdf").document
md = doc.export_to_markdown()
open("parsed_output.md", "w", encoding="utf-8").write(md)
print(md[:3000])