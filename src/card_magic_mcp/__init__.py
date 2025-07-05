import asyncio

from . import magic


def stdio():
    """Stdio entry point for the package."""
    asyncio.run(magic.stdio())


def sse():
    """SSE entry point for the package."""
    asyncio.run(magic.sse())


# Expose important items at package level
__all__ = ['stdio', 'sse', 'magic']
