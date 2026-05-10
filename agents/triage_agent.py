from langchain_core.prompts import ChatPromptTemplate

from prompts.prompts import TRIAGE_PROMPT
from utils.llm import llm

prompt = ChatPromptTemplate.from_template(TRIAGE_PROMPT)

chain = prompt | llm


def classify_ticket(ticket: str):
    response = chain.invoke({
        "ticket": ticket
    })

    return response.content.strip().lower()