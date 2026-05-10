from langchain_core.prompts import ChatPromptTemplate

from prompts.prompts import SENTIMENT_PROMPT
from utils.llm import llm

prompt = ChatPromptTemplate.from_template(SENTIMENT_PROMPT)

chain = prompt | llm


def analyze_sentiment(ticket: str):
    response = chain.invoke({
        "ticket": ticket
    })

    return response.content.strip().lower()