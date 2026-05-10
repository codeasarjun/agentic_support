import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
TEMPERATURE = float(os.getenv("TEMPERATURE"))

llm = ChatOllama(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)