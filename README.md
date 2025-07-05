# card-magic-mcp

[![License](https://img.shields.io/github/license/luochang212/card-magic-mcp)](https://github.com/luochang212/card-magic-mcp)
[![PyPI](https://img.shields.io/pypi/v/card-magic-mcp.svg?logo=python)](https://pypi.python.org/pypi/card-magic-mcp)
[![GitHub](https://img.shields.io/github/v/release/luochang212/card-magic-mcp?logo=github&sort=semver)](https://github.com/luochang212/card-magic-mcp)
[![CI](https://github.com/luochang212/card-magic-mcp/workflows/CI/badge.svg)](https://github.com/luochang212/card-magic-mcp/actions?query=workflow:CI)
[![Downloads](https://static.pepy.tech/personalized-badge/card-magic-mcp?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/card-magic-mcp)

[中文文档](https://github.com/luochang212/card-magic-mcp/blob/main/docs/README_CN.md)

A Model Context Protocol (MCP) server that implements the Chico and Dico card magic trick algorithm. This server enables AI assistants to perform mathematical card magic by encoding and decoding card sequences based on combinatorial principles. The magic works by using the first 4 cards to predict the 5th card from any randomly selected 5-card hand, leveraging factorial number systems and permutation mathematics.

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

### With Qwen Agent

Add this to `function_list` argument:

```json
{
  "mcpServers": {
    "card_magic": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "card-magic-mcp",
        "card_magic_mcp"
      ]
    }
  }
}
```

### With Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "card_magic": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/card_magic_mcp",
        "run",
        "card_magic_mcp"
      ]
    }
  }
}
```

## 🔧 Available Tools

The MCP Server provides two main tools for card magic:

- **`encode_cards`**: Encode 5 cards to hide the 5th card's information in the first 4
- **`decode_cards`**: Decode the hidden 5th card from the arrangement of 4 visible cards

## 🃏 Card Format

- **Suits**: ♠ (Spades), ♥ (Hearts), ♦ (Diamonds), ♣ (Clubs)
- **Ranks**: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
- **Format**: Each card should be written as `{suit}{rank}` with spaces separating multiple cards