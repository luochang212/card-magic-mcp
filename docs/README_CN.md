# card-magic-mcp

[![License](https://img.shields.io/github/license/luochang212/card-magic-mcp)](https://github.com/luochang212/card-magic-mcp)
[![PyPI](https://img.shields.io/pypi/v/card-magic-mcp.svg?logo=python)](https://pypi.python.org/pypi/card-magic-mcp)
[![GitHub](https://img.shields.io/github/v/release/luochang212/card-magic-mcp?logo=github&sort=semver)](https://github.com/luochang212/card-magic-mcp)
[![CI](https://github.com/luochang212/card-magic-mcp/workflows/CI/badge.svg)](https://github.com/luochang212/card-magic-mcp/actions?query=workflow:CI)
[![Downloads](https://static.pepy.tech/personalized-badge/card-magic-mcp?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/card-magic-mcp)

一个实现了 Chico & Dico 纸牌魔术的模型上下文协议服务 (MCP Server)。

> **Chico & Dico 的纸牌魔术**: 随机抽取五张扑克牌，观众只需按 Chico 整理好的顺序念出前四张牌，Dico 能知道第五张牌是什么。

## 一、安装

### 手动安装

```bash
pip install card-magic-mcp
```

### 通过 Smithery 安装

通过 [Smithery](https://smithery.ai/server/@luochang212/card-magic-mcp) 为 Claude Desktop 安装 Card Magic MCP Server：

```bash
npx -y @smithery/cli@latest install @luochang212/card-magic-mcp --client claude
```

## 二、使用方法

可通过 [Qwen Agent](https://github.com/QwenLM/Qwen-Agent) 调用，支持两种调用方法：`stdio`, `sse`，使用方法参见 [examples/usage_remote.py](../examples/usage_remote.py)

### 1. `stdio` 本地调用

将以下配置添加到 `function_list` 参数：

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

### 2. `sse` 远程调用

调用前，需在命令行运行以下代码，启动 MCP 服务：

```bash
uvx --from card-magic-mcp card_magic_sse
```

在 `function_list` 中添加以下配置：

```json
{
  "mcpServers": {
    "card_magic_sse": {
      "url": "http://0.0.0.0:8385/sse"
    }
  }
}
```

## 三、可用工具

MCP Server 为纸牌魔术提供两个工具：

- **`encode_cards`**：编码 5 张牌，将第 5 张牌的信息隐藏在前 4 张牌的排序信息中
- **`decode_cards`**：通过前 4 张牌的排列信息解码出隐藏的第 5 张牌

## 四、卡牌格式

- **花色**：`♠`（黑桃），`♥`（红心），`♦`（方块），`♣`（梅花）
- **点数**：`A，2，3，4，5，6，7，8，9，10，J，Q，K`
- **格式**：每张牌应写为 `{花色}{点数}`，多张牌之间用空格分隔
