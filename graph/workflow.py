
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
    return {"category": category}


def billing_node(state: SupportState):
    response = handle_billing(state["ticket"])
    return {"response": response}


def technical_node(state: SupportState):
    response = handle_technical(state["ticket"])
    return {"response": response}


def faq_node(state: SupportState):
    response = handle_faq(state["ticket"])
    return {"response": response}


def sentiment_analysis_node(state: SupportState):
    sentiment = analyze_sentiment(state["ticket"])
    return {"sentiment": sentiment}


def escalation_check_node(state: SupportState):
    escalation = check_escalation(
        state["ticket"],
        state["sentiment"]
    )
    return {"escalation": escalation}



def route_ticket(state: SupportState):

    category = state["category"]

    if category in ["billing", "refund"]:
        return "billing"

    elif category == "technical":
        return "technical"

    else:
        return "faq"



graph = StateGraph(SupportState)

# Nodes (IMPORTANT: no conflicts with state keys)

graph.add_node("triage", triage_node)
graph.add_node("billing", billing_node)
graph.add_node("technical", technical_node)
graph.add_node("faq", faq_node)

graph.add_node("sentiment_analysis", sentiment_analysis_node)
graph.add_node("escalation_check", escalation_check_node)

# Entry point
graph.set_entry_point("triage")

# Routing after triage
graph.add_conditional_edges(
    "triage",
    route_ticket,
    {
        "billing": "billing",
        "technical": "technical",
        "faq": "faq"
    }
)

# Flow: response → sentiment → escalation
graph.add_edge("billing", "sentiment_analysis")
graph.add_edge("technical", "sentiment_analysis")
graph.add_edge("faq", "sentiment_analysis")

graph.add_edge("sentiment_analysis", "escalation_check")
graph.add_edge("escalation_check", END)

workflow = graph.compile()