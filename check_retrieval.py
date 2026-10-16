from app.rag.retriever import retriever
for d in retriever.invoke("mtech 4th semester syllabus"):
    print(d.metadata.get("source"))
    print(d.page_content[:300])
    print("-----")