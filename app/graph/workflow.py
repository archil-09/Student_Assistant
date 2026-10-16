import os
from typing import Literal, TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel

from app.rag.retriever import rag_chain
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # app/rag/
ROOT_DIR = BASE_DIR.parents[1]  # student_assistant/

load_dotenv(dotenv_path=ROOT_DIR / ".env")
# student_assistant/

# ---------- LLM (used only for classifying the question) ----------
model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.0,
    model="openai/gpt-oss-120b",
)

QueryType = Literal[
    "student policies",
    "hostel rules",
    "placement guidelines",
    "admission_faq",
    "scholarship details",
    "not classified",
]


class Query(BaseModel):
    query_type: QueryType


structured_model = model.with_structured_output(Query)


# ---------- State ----------
class ReviewState(TypedDict):
    query: str
    query_type: QueryType
    response: str


# ---------- Helpers ----------
def _to_text(result) -> str:
    """rag_chain.invoke may return a str, an AIMessage, or a dict."""
    if isinstance(result, str):
        return result
    if hasattr(result, "content"):
        return result.content
    if isinstance(result, dict):
        for key in ("answer", "result", "output", "response"):
            if key in result:
                return str(result[key])
    return str(result)


def ask_rag(state: ReviewState) -> dict:
    result = rag_chain.invoke({"input": state["query"]})
    return {"response": _to_text(result)}
# ---------- Nodes ----------
def check_query_type(state: ReviewState) -> dict:
    result = structured_model.invoke(state["query"])
    return {"query_type": result.query_type}


def not_classified(state: ReviewState) -> dict:
    return {
        "response": "Sorry, I can only help with student policies, hostel rules, "
        "placement guidelines, admissions and scholarships."
    }


# One node per category; all use RAG for now, split them later if needed
student_policies = ask_rag
hostel_rules = ask_rag
placement_guidelines = ask_rag
admission_faq = ask_rag
scholarship_details = ask_rag


def route_query(state: ReviewState) -> str:
    return state["query_type"]


# ---------- Graph ----------
graph = StateGraph(ReviewState)

graph.add_node("check query type", check_query_type)
graph.add_node("student policies", student_policies)
graph.add_node("hostel rules", hostel_rules)
graph.add_node("placement guidelines", placement_guidelines)
graph.add_node("admission_faq", admission_faq)
graph.add_node("scholarship details", scholarship_details)
graph.add_node("not classified", not_classified)

graph.add_edge(START, "check query type")
graph.add_conditional_edges(
    "check query type",
    route_query,
    [
        "student policies",
        "hostel rules",
        "placement guidelines",
        "admission_faq",
        "scholarship details",
        "not classified",
    ],
)

for node in [
    "student policies",
    "hostel rules",
    "placement guidelines",
    "admission_faq",
    "scholarship details",
    "not classified",
]:
    graph.add_edge(node, END)

workflow = graph.compile()


if __name__ == "__main__":
    out = workflow.invoke({"query": "admission startings ?"})
    print(out["query_type"])
    print(out["response"])




