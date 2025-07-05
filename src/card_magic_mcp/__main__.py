import asyncio
import os

from . import server


host = os.getenv('HOST', '127.0.0.1')
port = int(os.getenv('PORT', 8000))


def stdio():
    """Stdio entry point for the package."""
    asyncio.run(server.mcp.run(transport="stdio"))


def http():
    """streamable-http entry point for the package."""
    asyncio.run(server.mcp.run(transport="http",
                               host=host,
                               port=port,
                               path="/mcp"))


def sse():
    """SSE entry point for the package."""
    asyncio.run(server.mcp.run(transport="sse",
                               host=host,
                               port=port))


if __name__ == "__main__":
    sse()
