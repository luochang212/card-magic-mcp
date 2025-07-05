import asyncio

from . import sse


def main():
    """SSE entry point for the package."""
    asyncio.run(sse.sse())


if __name__ == "__main__":
    main()
