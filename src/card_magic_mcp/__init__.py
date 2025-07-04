import asyncio

from . import magic


def main():
    """Main entry point for the package."""
    asyncio.run(magic.main())


# Expose important items at package level
__all__ = ['main', 'magic']
