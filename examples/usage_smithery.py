import os

from dotenv import load_dotenv
import mcp
from mcp.client.streamable_http import streamablehttp_client


# 加载 .env 文件中的环境变量
load_dotenv()


smithery_api_key = os.getenv('SMITHERY_API_KEY')
url = f"https://server.smithery.ai/@luochang212/card-magic-mcp/mcp?api_key={smithery_api_key}"


async def main():
    # Connect to the server using HTTP client
    async with streamablehttp_client(url) as (read_stream, write_stream, _):
        async with mcp.ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools_result = await session.list_tools()
            print(f"Available tools: {', '.join([t.name for t in tools_result.tools])}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
