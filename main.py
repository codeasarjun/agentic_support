
from graph.workflow import workflow
from database.db import init_db, save_ticket
from memory.chat_memory import save_chat

init_db()

print("\n=== Multi-Agent Customer Support System ===\n")

while True:
    ticket = input("Enter Support Ticket: ")

    if ticket.lower() == "exit":
        break

    result = workflow.invoke({
        "ticket": ticket
    })

    print("\n========== RESULT ==========")
    print(f"Category   : {result['category']}")
    print(f"Sentiment  : {result['sentiment']}")
    print(f"Escalation : {result['escalation']}")
    print("\nResponse:\n")
    print(result["response"])

    save_chat(ticket, result["response"])

    save_ticket(
        ticket=ticket,
        category=result["category"],
        sentiment=result["sentiment"],
        response=result["response"],
        escalation=result["escalation"]
    )

    print("\n============================\n")