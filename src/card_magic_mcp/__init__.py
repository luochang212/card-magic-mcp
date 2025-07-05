import asyncio

from . import magic


def main():
    """Stdio entry point for the package."""
    asyncio.run(magic.stdio())


def sse():
    """SSE entry point for the package."""
    asyncio.run(magic.sse())


# Expose important items at package level
__all__ = ['main', 'sse', 'magic']
