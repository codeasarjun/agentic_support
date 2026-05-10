from langchain_core.prompts import ChatPromptTemplate

from prompts.prompts import TECHNICAL_PROMPT
from utils.llm import llm

prompt = ChatPromptTemplate.from_template(TECHNICAL_PROMPT)

chain = prompt | llm


def handle_technical(ticket: str):
    response = chain.invoke({
        "ticket": ticket
    })

    return response.content