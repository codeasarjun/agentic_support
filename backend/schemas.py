from pydantic import BaseModel

class TicketRequest(BaseModel):
    ticket: str

class TicketResponse(BaseModel):
    category: str
    sentiment: str
    response: str
    escalate: bool
    escalation_reason: str