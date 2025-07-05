# -*- coding: utf-8 -*-

"""
Card Magic Agent

ENV:
  - uv pip install -U "qwen-agent[gui,rag,code_interpreter,mcp]"
  - uv pip install python-dotenv
"""

import os

from dotenv import load_dotenv
from qwen_agent.agents import Assistant, ReActChat


# 加载 .env 文件中的环境变量
load_dotenv()


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
    api_url = os.getenv('DEEPSEEK_API_URL')
    api_key = os.getenv('DEEPSEEK_API_KEY')

    # llm 配置
    llm_cfg = {
        'model': 'deepseek-reasoner',
        'model_server': api_url,
        'api_key': api_key,
    }

    # 实例化 CMAgent
    cma = CMAgent(llm_cfg)

    # 创建 Agent
    magic_agent = cma.create_react_agent()

    # 变魔术
    # query = "帮我编码 ♠2 ♠4 ♣2 ♦3 ♦7"
    query = "帮我编码 方片2 梅花J 黑桃2 红心3 方块K"
    msg = [
        {
            'role': 'user',
            'content': query
        }
    ]
    answer = cma.ask(magic_agent, msg)
    print(answer)
