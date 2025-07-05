# -*- coding: utf-8 -*-

"""
Card Magic Agent
"""

from qwen_agent.agents import Assistant, ReActChat


class CMAgent:
    """Card Magic Agent"""

    def __init__(self, llm_cfg):
        self.llm_cfg = llm_cfg

    @staticmethod
    def create_tools():
        """获取工具列表"""
        return [
            {
                "mcpServers": {
                    "card_magic": {
                        "type": "stdio",
                        "command": "uvx",
                        "args": [
                            "--from",
                            "card-magic-mcp",
                            "card_magic_mcp"
                        ],
                    }
                }
            },
        ]

    def create_react_agent(self):
        """创建 ReActChat 模式的 Agent"""
        tools = self.create_tools()
        return ReActChat(
            llm=self.llm_cfg,
            name='卡牌魔术助手',
            description='使用 ReActChat 模式',
            system_message='',
            function_list=tools,
        )

    def create_assistant_agent(self):
        """创建 Assistant 模式的 Agent"""
        tools = self.create_tools()
        return Assistant(
            llm=self.llm_cfg,
            name='卡牌魔术助手',
            description='使用 Assistant 模式',
            system_message='',
            function_list=tools,
        )

    @staticmethod
    def ask(bot, messages: list) -> str:
        """使用指定的 bot 进行查询"""
        response = bot.run_nonstream(messages)
        message = response[-1].get('content').strip()
        return message


if __name__ == '__main__':
    # llm 配置
    llm_cfg = {
        'model': 'Qwen3-0.6B-FP8',
        'model_server': 'http://localhost:8000/v1',
        'api_key': 'token-kcgyrk',
        'generate_cfg': {
            'top_p': 0.95,
            'temperature': 0.6,
        }
    }

    # 实例化 CMAgent
    cma = CMAgent(llm_cfg)

    # 创建 Agent
    magic_agent = cma.create_react_agent()
    # magic_agent = cma.create_assistant_agent()

    # 变魔术
    query = "帮我编码 ♠2 ♠4 ♣2 ♦3 ♦7"
    msg = [
        {
            'role': 'user',
            'content': query
        }
    ]
    answer = cma.ask(magic_agent, msg)
    print(answer)
