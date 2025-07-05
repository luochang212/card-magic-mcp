# -*- coding: utf-8 -*-

from fastmcp import FastMCP

from .magic import decode_cards, encode_cards


mcp = FastMCP("card_magic_sse")


@mcp.tool
async def encode_cards_tool(cards: str) -> str:
    """本函数实现魔术师 Chico 的操作：将五张牌重新排序，
    并在排序过程中将第五张牌的信息编码在前四张的排序信息中

    :param cards: 该参数接受 5 张牌，形如 ♥K ♣3 ♠7 ♦5 ♠A
                  每张牌由【花色】和【数字】组成：
                    - 可选的花色:
                      - ♠ (黑桃, Spades)
                      - ♥ (红心, Hearts)
                      - ♦ (方块/方片, Diamonds)
                      - ♣ (梅花, Clubs)
                    - 可选的数字: A 2 3 4 5 6 7 8 9 10 J Q K
                  注意：请将花色和数字标准化后再作为参数传入
    :return: 本函数返回前四张牌和第五张牌的值
    """
    return encode_cards(cards)


@mcp.tool
async def decode_cards_tool(cards: str) -> str:
    """本函数实现魔术师 Dico 的操作：根据前四张牌猜第五张牌

    :param cards: 该参数接受 4 张牌，形如 ♠A ♥3 ♣10 ♦K
                  每张牌由【花色】和【数字】组成：
                    - 可选的花色:
                      - ♠ (黑桃, Spades)
                      - ♥ (红心, Hearts)
                      - ♦ (方块/方片, Diamonds)
                      - ♣ (梅花, Clubs)
                    - 可选的数字: A 2 3 4 5 6 7 8 9 10 J Q K
                  注意：请将花色和数字标准化后再作为参数传入
    :return: 本函数返回第五张牌的值
    """
    return decode_cards(cards)


if __name__ == "__main__":
    mcp.run()
