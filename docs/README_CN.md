# card-magic-mcp

[![License](https://img.shields.io/github/license/luochang212/card-magic-mcp)](https://github.com/luochang212/card-magic-mcp)
[![PyPI](https://img.shields.io/pypi/v/card-magic-mcp.svg?logo=python)](https://pypi.python.org/pypi/card-magic-mcp)
[![GitHub](https://img.shields.io/github/v/release/luochang212/card-magic-mcp?logo=github&sort=semver)](https://github.com/luochang212/card-magic-mcp)
[![CI](https://github.com/luochang212/card-magic-mcp/workflows/CI/badge.svg)](https://github.com/luochang212/card-magic-mcp/actions?query=workflow:CI)
[![Downloads](https://static.pepy.tech/personalized-badge/card-magic-mcp?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/card-magic-mcp)

一个实现了 Chico & Dico 纸牌魔术的模型上下文协议（MCP）服务器。该服务器使AI助手能够通过基于组合原理的编码和解码纸牌序列来表演数学纸牌魔术。魔术的工作原理是使用前4张牌来预测从任何随机选择的5张牌中预测第5张牌，利用阶乘数系统和排列数学。

## 📦 安装

### 手动安装

```bash
pip install card-magic-mcp
```

### 通过Smithery安装

通过 [Smithery](https://smithery.ai/server/card-magic-mcp) 为 Claude Desktop 安装 Card Magic MCP Server：

```bash
npx -y @smithery/cli install card-magic-mcp --client claude
```

## 🚀 使用方法

### Claude Desktop

将此添加到您的 `claude_desktop_config.json` 中：

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

### Qwen Agent

将此添加到 `function_list` 参数中：

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

## 🔧 可用工具

MCP Server 为纸牌魔术提供两个工具：

- **`encode_cards`**：编码 5 张牌，将第 5 张牌的信息隐藏在前 4 张牌中
- **`decode_cards`**：通过前 4 张牌的排列信息，解码隐藏的第 5 张牌

## 🃏 纸牌格式

- **花色**：♠（黑桃），♥（红心），♦（方块），♣（梅花）
- **点数**：A，2，3，4，5，6，7，8，9，10，J，Q，K
- **格式**：每张牌应写为 `{花色}{点数}`，多张牌之间用空格分隔
