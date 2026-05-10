from langchain_core.prompts import ChatPromptTemplate

from prompts.prompts import FAQ_PROMPT
from utils.llm import llm

prompt = ChatPromptTemplate.from_template(FAQ_PROMPT)

chain = prompt | llm


def handle_faq(ticket: str):
    response = chain.invoke({
        "ticket": ticket
    })

    return response.content