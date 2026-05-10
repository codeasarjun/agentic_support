chat_history = []


def save_chat(ticket, response):
    chat_history.append({
        "ticket": ticket,
        "response": response
    })


def get_history():
    return chat_history