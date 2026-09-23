# The code below is used to create the virtual environment 

# uv add langchain langchain-google-genai python-dotenv

from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from rich.console import Console
from rich.markdown import Markdown

from tools import starter_tool

import uuid

agent = create_agent(
                model = "google_genai:gemini-3.6-flash",
                checkpointer= InMemorySaver(), 
                system_prompt = "return the number as a series of tallies, add previous numbers to the total"
              )

config = {"configurable": {"thread_id": str(uuid.uuid4())}}

console = Console()



# In main(), replace print(response) with:
# console.print(Markdown(response))

def get_response(prompt: str) -> str:
    response = agent.invoke({"messages": [{"role": "user", "content":prompt}]}
                 , config = config)
    return response["messages"][-1].text

def main():
    while True:
        try:
            prompt = input("Input: ")
            
            if prompt == "exit": break
            response = get_response(prompt)
        except EOFError:
            break
        console.print(Markdown(response))
#        print(response)

if __name__ == "__main__":
    main()