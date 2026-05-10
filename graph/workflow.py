from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.triage_agent import classify_ticket
from agents.sentiment_agent import analyze_sentiment
from agents.billing_agent import handle_billing
from agents.technical_agent import handle_technical
from agents.faq_agent import handle_faq
from agents.escalation_agent import check_escalation


class SupportState(TypedDict):
    ticket: str
    category: str
    sentiment: str
    response: str
    escalation: str


def triage_node(state: SupportState):
    category = classify_ticket(state["ticket"])

    return {
        "category": category
    }


def sentiment_node(state: SupportState):
    sentiment = analyze_sentiment(state["ticket"])

    return {
        "sentiment": sentiment
    }


def billing_node(state: SupportState):
    response = handle_billing(state["ticket"])

    return {
        "response": response
    }


def technical_node(state: SupportState):
    response = handle_technical(state["ticket"])

    return {
        "response": response
    }


def faq_node(state: SupportState):
    response = handle_faq(state["ticket"])

    return {
        "response": response
    }


def escalation_node(state: SupportState):
    escalation = check_escalation(
        state["ticket"],
        state["sentiment"]
    )

    return {
        "escalation": escalation
    }


def route_ticket(state: SupportState):
    category = state["category"]

    if category in ["billing", "refund"]:
        return "billing"

    elif category == "technical":
        return "technical"

    else:
        return "faq"


graph = StateGraph(SupportState)

graph.add_node("triage", triage_node)
graph.add_node("sentiment", sentiment_node)
graph.add_node("billing", billing_node)
graph.add_node("technical", technical_node)
graph.add_node("faq", faq_node)
graph.add_node("escalation", escalation_node)

graph.set_entry_point("triage")

graph.add_conditional_edges(
    "triage",
    route_ticket,
    {
        "billing": "billing",
        "technical": "technical",
        "faq": "faq"
    }
)

graph.add_edge("billing", "sentiment")
graph.add_edge("technical", "sentiment")
graph.add_edge("faq", "sentiment")

graph.add_edge("sentiment", "escalation")

graph.add_edge("escalation", END)

workflow = graph.compile()