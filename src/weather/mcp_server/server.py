# Do not use the FastMCP module coming with the Model Context Protocol SDK
# from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP

mcp = FastMCP(
    name='weather',
    instructions=(
        'This server provides weather report tools. Call the resource `resource://about` to get extra information.'
    ),
)
"""Weather MCP Server."""
