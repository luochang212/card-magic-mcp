# card-magic-mcp

[![License](https://img.shields.io/github/license/luochang212/card-magic-mcp)](https://github.com/luochang212/card-magic-mcp)
[![PyPI](https://img.shields.io/pypi/v/card-magic-mcp.svg?logo=python)](https://pypi.python.org/pypi/card-magic-mcp)
[![GitHub](https://img.shields.io/github/v/release/luochang212/card-magic-mcp?logo=github&sort=semver)](https://github.com/luochang212/card-magic-mcp)
[![CI](https://github.com/luochang212/card-magic-mcp/workflows/CI/badge.svg)](https://github.com/luochang212/card-magic-mcp/actions?query=workflow:CI)
[![Downloads](https://static.pepy.tech/personalized-badge/card-magic-mcp?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/card-magic-mcp)

[中文文档](https://github.com/luochang212/card-magic-mcp/blob/main/docs/README_CN.md)

A Model Context Protocol (MCP) server that implements the Chico & Dico card magic trick.

> **Chico & Dico's Card Magic**: Randomly draw five playing cards, and the audience only needs to recite the first four cards in the order arranged by Chico, and Dico can know what the fifth card is.

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
uvx --from card-magic-mcp card_magic_sse
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
