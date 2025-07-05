# card-magic-mcp

[![License](https://img.shields.io/github/license/luochang212/card-magic-mcp)](https://github.com/luochang212/card-magic-mcp)
[![PyPI](https://img.shields.io/pypi/v/card-magic-mcp.svg?logo=python)](https://pypi.python.org/pypi/card-magic-mcp)
[![Downloads](https://static.pepy.tech/personalized-badge/card-magic-mcp?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/card-magic-mcp)
[![CI](https://github.com/luochang212/card-magic-mcp/workflows/CI/badge.svg)](https://github.com/luochang212/card-magic-mcp/actions?query=workflow:CI)
[![smithery badge](https://smithery.ai/badge/@luochang212/card-magic-mcp)](https://smithery.ai/server/@luochang212/card-magic-mcp)

实现了 Chico & Dico 纸牌魔术的 MCP Server。魔术是这样的：观众随机抽五张扑克牌，然后交给魔术师 Chico 理一下牌，这时观众只需按 Chico 整理好的顺序念出前四张牌，魔术师 Dico 就能说出第五张牌是什么。

可以在 [**Smithery Playground**](https://smithery.ai/playground?prompt=connect%20to%20%40luochang212%2Fcard-magic-mcp) 体验这个魔术。

![smithery_playground](/img/smithery_playground.png)

表演步骤：

1. 跟魔术师说：`帮我整理这些扑克牌 ♠J ♠4 ♣2 ♦3 ♦K`
2. 这位魔术师会将这些牌分成两堆：前四张 和 第五张
3. 告诉另一位魔术师前四张牌是什么，他能说出第五张牌：`前四张扑克牌是 xxxx，请问第五张牌是什么？`

> [!NOTE]
> 相信我，它绝不是通过记忆获知第五张牌是什么，而是通过纯粹的魔法实现的。为了防止当前对话框记住第五张牌，你可以开一个新的 Playground 页面。告诉它前四张牌是什么，看看它还能不能猜对。

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

支持 [Qwen Agent](https://github.com/QwenLM/Qwen-Agent)，可通过两种方法调用：`stdio`, `sse`

> 具体使用方法参见：[examples/usage_remote.py](../examples/usage_remote.py)

### `stdio`: 本地调用

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

### `sse`: 远程调用

调用前，需在命令行运行以下代码，启动 MCP 服务：

```bash
HOST=0.0.0.0 PORT=8385 uvx --from card-magic-mcp card_magic_sse
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

## 四、纸牌格式

- **花色**：`♠`（黑桃），`♥`（红心），`♦`（方块），`♣`（梅花）
- **点数**：`A，2，3，4，5，6，7，8，9，10，J，Q，K`
- **格式**：每张牌应写为 `{花色}{点数}`，多张牌之间用空格分隔
