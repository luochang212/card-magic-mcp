import asyncio

from . import magic


def sse():
    """SSE entry point for the package."""
    asyncio.run(magic.sse())
