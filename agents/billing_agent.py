from langchain_core.prompts import ChatPromptTemplate

from prompts.prompts import BILLING_PROMPT
from utils.llm import llm

prompt = ChatPromptTemplate.from_template(BILLING_PROMPT)

chain = prompt | llm


def handle_billing(ticket: str):
    response = chain.invoke({
        "ticket": ticket
    })

    return response.content