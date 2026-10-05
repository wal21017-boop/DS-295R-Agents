# The code below is used to create the virtual environment 

# uv add langchain langchain-google-genai python-dotenv
import asyncio
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from rich.console import Console
from rich.markdown import Markdown
from langchain.chat_models import init_chat_model

from ds_295r_ai_agent_engineering.tools import starter_tool, ethics_manifesto
from ds_295r_ai_agent_engineering.ethics_agent import ethics_agent

from pathlib import Path

from langchain.mcp import MCPAdapter

import fastmcp

file_directory = Path(
    r"C:\Users\brian\OneDrive\Desktop\Fall 2026"
    r"\DS 295R - AI Agent Engineering"
    r"\src\ds_295r_ai_agent_engineering"
    r"\file_storage"
)
# An in-process FastMCP server: no subprocess, no socket. Ideal for tests.
# in_memory = MCPAdapter(server)  # a FastMCP instance

# A script path is launched over stdio, one subprocess per adapter.
# stdio = MCPAdapter(Path("MCP.py"))

# A string must be an http(s) URL, reached over streamable HTTP.

import uuid


config = {"configurable": {"thread_id": str(uuid.uuid4())}}





# In main(), replace print(response) with:
# console.print(Markdown(response))


def main():
    asyncio.run(_main())

async def _main():
    async def get_response(prompt: str) -> str:
        response = await agent.ainvoke({"messages": [HumanMessage(prompt)]}
                 , config = config)
        return response["messages"][-1].text
    servers = {"mcpServers":
                   {
                        "docs-langchain": {
                        "url": "https://docs.langchain.com/mcp"
                        },
                        "reference-langchain": {
                        "url": "https://reference.langchain.com/mcp"
                        },
                        "files": {                                                                                                       
                            "command": "cmd.exe",
                            "args": [
                                "/c",
                                "npx",
                                "-y",
                                "@modelcontextprotocol/server-filesystem",
                                str(file_directory)
                                ]
                        }                                                                                                                
                    }
    }
    async with MCPAdapter(servers) as adapter:
        mcp_tools = await adapter.list_tools()


        console = Console()


    
        model = init_chat_model(
                        model = "google_genai:gemini-flash-lite-latest"
                        # model = "google_genai:gemini-3.7-flash"
                        # model = "gemini-3.1-pro-preview"
                        # model = ""
                        #, thinking_level = "high"
                        #, thinking_level = "minimal"
                        )

        agent = create_agent(
                model = model,
                checkpointer= InMemorySaver(), 
                tools= [ethics_manifesto, ethics_agent, *mcp_tools],
#                tools=mcp_tools,
                system_prompt = " Always refer to the ethics agent for guidance."
              )

        while True:
            try:
                prompt = input("Input: ")
            
                if prompt == "exit": break
                response = await get_response(prompt)
            except EOFError:
                break
            console.print(Markdown(response))
#        print(response)




if __name__ == "__main__":
    main()