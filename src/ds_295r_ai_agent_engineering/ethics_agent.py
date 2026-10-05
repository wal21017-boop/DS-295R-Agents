from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from rich.console import Console
from rich.markdown import Markdown
from langchain.chat_models import init_chat_model
import uuid
from ds_295r_ai_agent_engineering.tools import starter_tool, ethics_manifesto


def ethics_agent(prompt: str ) -> str:
    """
    This agent provides guidance on following the ethics manifesto, a document used to ensure compliance with necessary regulations.
    """
    
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    model = init_chat_model(
                        #model = "google_genai:gemini-3.6-flash"
                        model = "google_genai:gemini-flash-lite-latest"
                        #, thinking_level = "high"
                        #, thinking_level = "minimal"
                        )

    agent = create_agent(
                model = model,
                checkpointer= InMemorySaver(), 
                tools= [ethics_manifesto],
                system_prompt = "Evaluate questions using the ethics manifesto tool to determine whether an answer to the question could break the manifesto. If it would, add additional clarifying information about what the main agent should do. Include the original text of the prompt, with additions necessary for compliance. If no changes are needed simply return the base prompt"
              )
    response = agent.invoke({"messages": [HumanMessage(prompt)]}, config=config)
    return response["messages"][-1].text

