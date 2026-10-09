from dotenv import load_dotenv
load_dotenv()
import asyncio
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from rich.console import Console
from rich.markdown import Markdown
from langchain.chat_models import init_chat_model
import uuid
from ds_295r_ai_agent_engineering.tools import starter_tool, ethics_manifesto
from langchain.mcp import MCPAdapter


def korean_agent(prompt: str ) -> str:
    """
    This agent provides korean tutoring. It converses with the user, providing helpful tips and hints, while providing definitions for unfamiliar words.
    """
#    servers = {"mcpServers":
#                       {
#                            "korean dictionary": {
#                            "url": "https://korean.dict.naver.com/koendict/#/main"
#                            }
#                      }
#                }
#    async with MCPAdapter(servers) as adapter:
#            mcp_tool = await adapter.list_tools()
    
    
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
                tools= [],
                system_prompt = "You are a korean tutor. Converse with me in Korean, but provide help in English if necessary."
              )
    response = agent.invoke({"messages": [HumanMessage(prompt)]}, config=config)
    return response["messages"][-1].text

