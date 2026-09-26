from config import GROQ_API_KEY, EMBED_MODEL_ID, CHROMA_DIR
import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL_ID)

vectorstore = Chroma(
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings,
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

llm = ChatGroq(api_key=GROQ_API_KEY, model="openai/gpt-oss-120b", temperature=0)

prompt = ChatPromptTemplate.from_template(
    """Answer based only on the following context.
If the answer isn't in the context, say you don't know.

Context:
{context}

Question: {input}
"""
)

rag_chain = create_retrieval_chain(
    retriever, create_stuff_documents_chain(llm, prompt)
)

def ask(query: str):
    return rag_chain.invoke({"input": query})

if __name__ == "__main__":
    result = ask("Does the institute support extracurricular activities?")
    print(result["answer"])