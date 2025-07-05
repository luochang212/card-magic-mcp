# -*- coding: utf-8 -*-

import asyncio

from mcp.server import Server
from mcp.server.sse import SseServerTransport
from mcp.types import TextContent, Tool
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Mount, Route
import uvicorn

from .magic import CardGame, create_logger


# Initialize server
app = Server("card_magic_mcp")

# Configure logging
logger = create_logger("card_magic_mcp")


cg = CardGame()


@app.list_tools()
async def list_tools() -> list[Tool]:
    """列出可用工具"""
    logger.info("Listing tools...")
    return [
        Tool(
            name="encode_cards",
            description='\n'.join([
                "魔术师Chico: 将5张牌重新排序",
                "该函数接受5张牌，每张牌由【花色】和【数字】组成。",
                "- 可选的花色: ♠(黑桃) ♥(红心) ♦(方块/方片) ♣(梅花)",
                "- 可选的数字: A 2 3 4 5 6 7 8 9 10 J Q K",
                '输入示例: {"cards": "♥K ♣3 ♠7 ♦5 ♠A"}',
            ]),
            inputSchema={
                "type": "object",
                "properties": {
                    "cards": {
                        "type": "string",
                        "description": "5张牌的值"
                    }
                },
                "required": ["cards"]
            }
        ),
        Tool(
            name="decode_cards",
            description='\n'.join([
                "魔术师Dico: 根据前4张牌猜第5张牌",
                "该函数接受4张牌，每张牌由【花色】和【数字】组成。",
                "- 可选的花色: ♠(黑桃) ♥(红心) ♦(方块/方片) ♣(梅花)",
                "- 可选的数字: A 2 3 4 5 6 7 8 9 10 J Q K",
                '输入示例: {"cards": "♠A ♥3 ♣10 ♦K"}',
            ]),
            inputSchema={
                "type": "object",
                "properties": {
                    "cards": {
                        "type": "string",
                        "description": "4张牌的值"
                    }
                },
                "required": ["cards"]
            }
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """执行编码/解码工具"""
    logger.info(f"Calling tool: {name} with arguments: {arguments}")

    if name not in ("encode_cards", "decode_cards"):
        raise ValueError(f"Unknown tool: {name}")

    card_str = arguments.get("cards")
    if not card_str:
        raise ValueError("Cards is required")

    # 解析卡面信息
    try:
        cards = [card.strip() for card in card_str.strip().split() if card.strip()]
    except Exception as e:
        logger.warning(f"卡面信息解析失败: {str(e)}")
        return [TextContent(type="text", text=f"卡面信息解析失败: {str(e)}")]

    # 检查卡面信息
    card_cnt = 4 if name == "decode_cards" else 5
    check_info = cg.check_card(cards, card_num=card_cnt)

    if check_info != "pass":
        logger.warning(check_info)
        return [TextContent(type="text", text=check_info)]

    if name == "encode_cards":
        res = cg.chico(cards)
    else:
        res = cg.dico(cards)

    return [TextContent(type="text", text=res)]


def create_starlette_app(mcp_server: Server, *, debug: bool = False) -> Starlette:
    """创建 Starlette 应用程序"""
    sse = SseServerTransport("/messages/")

    async def handle_sse(request: Request) -> None:
        async with sse.connect_sse(
                request.scope,
                request.receive,
                request._send,
        ) as (read_stream, write_stream):
            await mcp_server.run(
                read_stream,
                write_stream,
                mcp_server.create_initialization_options(),
            )

    return Starlette(
        debug=debug,
        routes=[
            Route("/sse", endpoint=handle_sse),
            Mount("/messages/", app=sse.handle_post_message),
        ],
    )


async def sse(host="0.0.0.0", port=8385):
    """SSE 入口"""
    logger.info(f"Running in SSE mode on http://{host}:{port}")

    starlette_app = create_starlette_app(app, debug=True)

    config = uvicorn.Config(
        app=starlette_app,
        host=host,
        port=port,
        log_level="info",
        loop="asyncio"
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(sse())
