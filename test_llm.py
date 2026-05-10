
from utils.llm import llm

response = llm.invoke(
    "Hello"
)

print(response.content)