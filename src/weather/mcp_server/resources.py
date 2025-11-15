import os

import aiofiles

from mcp_server.server import mcp


@mcp.resource(
    'resource://about',
    description='Get the about content.',
)
async def get_about() -> str:
    """Get the about content."""
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'about.md'))
    async with aiofiles.open(filename, 'r') as file:
        return await file.read()
