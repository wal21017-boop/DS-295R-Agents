from pathlib import Path
from langchain.mcp import MCPAdapter
import asyncio

FILE_DIR = Path(
    r"C:\Users\brian\OneDrive\Desktop\Fall 2026"
    r"\DS 295R - AI Agent Engineering"
    r"\src\ds_295r_ai_agent_engineering"
    r"\file_storage"
)

print(FILE_DIR)
print(FILE_DIR.exists())
print(FILE_DIR.is_dir())

if not FILE_DIR.is_dir():
    raise FileNotFoundError(FILE_DIR)

file_server = {
    "mcpServers": {
        "files": {
            "command": "cmd.exe",
            "args": [
                "/d",
                "/s",
                "/c",
                "npx.cmd -y @modelcontextprotocol/server-filesystem "
                f'"{FILE_DIR}"',
            ],
        }
    }
}

async def test_files():
    async with MCPAdapter(file_server) as adapter:
        tools = await adapter.list_tools()
        print("File tools:")
        for tool in tools:
            print("-", tool.name)

if __name__ == "__main__":
    asyncio.run(test_files())

    