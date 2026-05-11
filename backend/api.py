from fastapi import FastAPI

from backend.schemas import (
    TicketRequest,
    TicketResponse
)

from graph.workflow import workflow
api = FastAPI()

@api.post("/support-ticket", response_model=TicketResponse)
def process_ticket(data: TicketRequest):

    initial_state = {
        "ticket": data.ticket,
        "agent_logs": []
    }

    result = workflow.invoke(initial_state)

    return {
        "category": result["category"],
        "sentiment": result["sentiment"],
        "response": result["response"],
        "escalate": result["escalate"],
        "escalation_reason": result["escalation_reason"]
    }