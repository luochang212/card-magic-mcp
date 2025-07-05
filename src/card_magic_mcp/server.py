# -*- coding: utf-8 -*-

from fastmcp import FastMCP

from .magic import decode_cards, encode_cards


mcp = FastMCP("card_magic_sse")


encode_cards = mcp.tool(encode_cards)
decode_cards = mcp.tool(decode_cards)


if __name__ == "__main__":
    mcp.run()
