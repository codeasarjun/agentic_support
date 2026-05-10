
from langchain_core.prompts import ChatPromptTemplate

from prompts.prompts import ESCALATION_PROMPT
from utils.llm import llm

prompt = ChatPromptTemplate.from_template(ESCALATION_PROMPT)

chain = prompt | llm


def check_escalation(ticket: str, sentiment: str):
    response = chain.invoke({
        "ticket": ticket,
        "sentiment": sentiment
    })

    return response.content.strip().lower()