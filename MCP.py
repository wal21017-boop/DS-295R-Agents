from langchain.agents import create_agent
from langchain.mcp import MCPAdapter

http = MCPAdapter("https://docs.langchain.com/mcp")

async def main():
    async with http as adapter:
        tools = await adapter.list_tools()
        agent = create_agent("google_genai:gemini-3.6-flash", tools)
        return await agent.ainvoke({"messages": [{"role": "user", "content": "..."}]})


    {
  "servers": {
    "docs-langchain": {
      "url": "https://docs.langchain.com/mcp"
    },
    "reference-langchain": {
      "url": "https://reference.langchain.com/mcp"
    }
  }
}

# Define a tool for the LLM to call
@http.tool()
def get_docs(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    http.run(transport="http")