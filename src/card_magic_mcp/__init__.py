import asyncio

from . import server


def main():
    """Stdio entry point for the package."""
    asyncio.run(server.mcp.run())


# Expose important items at package level
__all__ = ['main', 'server']
