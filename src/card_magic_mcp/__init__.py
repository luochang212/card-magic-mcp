import asyncio

from . import sse, stdio


def main():
    """Stdio entry point for the package."""
    asyncio.run(stdio.stdio())


# Expose important items at package level
__all__ = ['main', 'sse', 'stdio']
