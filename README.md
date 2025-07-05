# card-magic-mcp

[![License](https://img.shields.io/github/license/luochang212/card-magic-mcp)](https://github.com/luochang212/card-magic-mcp)
[![PyPI](https://img.shields.io/pypi/v/card-magic-mcp.svg?logo=python)](https://pypi.python.org/pypi/card-magic-mcp)
[![Downloads](https://static.pepy.tech/personalized-badge/card-magic-mcp?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/card-magic-mcp)
[![CI](https://github.com/luochang212/card-magic-mcp/workflows/CI/badge.svg)](https://github.com/luochang212/card-magic-mcp/actions?query=workflow:CI)
[![smithery badge](https://smithery.ai/badge/@luochang212/card-magic-mcp)](https://smithery.ai/server/@luochang212/card-magic-mcp)

[中文文档](https://github.com/luochang212/card-magic-mcp/blob/main/docs/README_CN.md)

A Model Context Protocol (MCP) server that implements the Chico & Dico card magic trick.

> **Chico & Dico's Card Magic**: Randomly draw five playing cards, and the audience only needs to recite the first four cards in the order arranged by Chico, and Dico can know what the fifth card is.

You can experience this magic trick in the [**Smithery Playground**](https://smithery.ai/playground?prompt=connect%20to%20%40luochang212%2Fcard-magic-mcp).

![smithery_playground](/img/smithery_playground.png)

## 🎭 Performance Steps

1. Tell the magician: `Help me arrange these playing cards ♠J ♠4 ♣2 ♦3 ♦K`
2. This magician will separate the cards into two piles: the first four cards and the fifth card
3. Tell the other magician what the first four cards are, and they can tell you what the fifth card is: `The first four playing cards are [card1 card2 card3 card4], what is the fifth card?`

> [!NOTE]
> Trust me, it's not through memory that it knows what the fifth card is, but through pure magic. To prevent the current dialog from remembering the fifth card, you can open a new Playground page. Tell it what the first four cards are and see if it can still guess correctly.

## 📦 Installation

### Manual Installation

```bash
pip install card-magic-mcp
```

### Installing via Smithery

To install Card Magic MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@luochang212/card-magic-mcp):

```bash
npx -y @smithery/cli@latest install @luochang212/card-magic-mcp --client claude
```

## 🚀 Usage

This MCP server can be integrated with [Qwen Agent](https://github.com/QwenLM/Qwen-Agent) using two connection methods: `stdio` and `sse`.

> For more examples, see [examples/usage_remote.py](examples/usage_remote.py)

### `stdio`: Local Call

Add the following configuration to the `function_list` parameter:

```json
{
  "mcpServers": {
    "card_magic": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "card-magic-mcp",
        "card_magic_stdio"
      ]
    }
  }
}
```

### `sse`: Remote Call

Before calling, run the following code in the command line to start the MCP service:

```bash
HOST=0.0.0.0 PORT=8385 uvx --from card-magic-mcp card_magic_sse
```

Add the following configuration to `function_list`:

```json
{
  "mcpServers": {
    "card_magic_sse": {
      "url": "http://0.0.0.0:8385/sse"
    }
  }
}
```

## 🔧 Available Tools

The MCP Server provides two tools for card magic:

- **`encode_cards`**: Encode 5 cards to hide the 5th card's information in the arrangement of the first 4 cards
- **`decode_cards`**: Decode the hidden 5th card from the arrangement information of the first 4 visible cards

## 🃏 Card Format

- **Suits**: `♠` (Spades), `♥` (Hearts), `♦` (Diamonds), `♣` (Clubs)
- **Ranks**: `A，2，3，4，5，6，7，8，9，10，J，Q，K`
- **Format**: Each card should be written as `{suit}{rank}` with spaces separating multiple cards
