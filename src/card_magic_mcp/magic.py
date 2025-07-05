# -*- coding: utf-8 -*-

from functools import lru_cache
import logging
import random
from typing import Tuple


def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


@lru_cache(maxsize=128)
def factorial(n):
    """计算n的阶乘"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


class MagicMax:
    """Chico 和 Dico 的魔术 - 推广版"""

    def __init__(self, n, k):
        assert 3 <= k
        assert k <= n < factorial(k) + k
        self.n = n  # 整个牌组有多少牌
        self.k = k  # 从牌组中抽几张牌

    @staticmethod
    def reverse(cards):
        """翻转牌组，分出前 k - 1 张牌"""
        reversed_cards = cards[::-1]
        return reversed_cards[:-1], reversed_cards[-1]

    def encoder(self, cards):
        """将第 k 张牌的牌面信息编码到前 k-1 张的顺序中"""
        res = []
        cards = sorted(cards)
        s = sum(cards) % factorial(self.k)

        q = s
        for i in range(self.k, 0, -1):
            q, r = divmod(q, i)
            res.append(cards.pop(r))
        return res

    def decoder(self, visible_cards):
        """将第 k 张牌的牌面信息从前 k-1 张牌的排列信息中解码出来"""
        # 逆向求解编码过程
        q, r = 0, 0
        for i in range(1, self.k):
            q = i * q + r

            if i < self.k - 1:  # 前 k-2 步需要计算余数
                r = sorted(visible_cards[:i+1]).index(visible_cards[i])

        # 判断模 k! 的偏离量 t
        sum_visible_cards = sum(visible_cards)
        factorial_k = factorial(self.k)

        epoch = sum([self.n - i for i in range(self.k)]) // factorial_k
        for t in range(epoch + 1):
            v_guess = self.k * q + t * factorial_k - sum_visible_cards
            if 1 <= v_guess <= self.n:
                break

        for r in range(self.k):
            # 线索1：牌组总和为 s + k! * t
            s = self.k * q + r
            v = s + factorial_k * t - sum_visible_cards
            # 线索2：第 k 张牌的值 v 放入牌组中获得正确的余数 r
            if 1 <= v <= self.n and v not in visible_cards:
                real_r = sorted(visible_cards + [v]).index(v)
                if real_r == r:
                    return v


class CardMapper:
    """数字和扑克牌的双向映射"""

    def __init__(self):
        self.suits = ['♠', '♥', '♦', '♣']  # 黑桃 红心 方块 梅花
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self._num_to_card = dict()
        self._card_to_num = dict()

        num = 1
        for suit in self.suits:
            for rank in self.ranks:
                card = f'{suit}{rank}'
                self._num_to_card[num] = card
                self._card_to_num[card] = num
                num += 1

    def num_to_card(self, num: int) -> str:
        """将1-52的数字转换为扑克牌"""
        if not (1 <= num <= 52):
            raise ValueError(f'num must be between [1, 52]. Invalid num: {num}')
        return self._num_to_card[num]

    def card_to_num(self, card: str) -> int:
        """将扑克牌转换为1-52的数字"""
        if card not in self._card_to_num:
            raise ValueError(f'Invalid card: {card}')
        return self._card_to_num[card]

    def get_suit_and_rank(self, num: int) -> Tuple[str, str]:
        """根据指定的数字分别获取花色和点数"""
        if not (1 <= num <= 52):
            raise ValueError(f'num must be between [1, 52]. Invalid num: {num}')

        suit_index = (num - 1) // 13
        rank_index = (num - 1) % 13
        return self.suits[suit_index], self.ranks[rank_index]

    def is_card(self, card: str) -> bool:
        return (card in self._card_to_num)

    def random_n_cards(self, n: int = 5):
        assert 1 <= n <= len(self._card_to_num)
        n_cards = random.sample(self._card_to_num.keys(), n)
        return ' '.join(n_cards)

    def display_all_mapping(self):
        """显示所有数字到扑克牌的映射"""
        print('数字 -> 扑克牌：')
        for i in range(1, 53):
            suit, rank = self.get_suit_and_rank(i)
            print(f'{i:2d} -> {suit}{rank}')


class CardGame:
    """游戏交互"""

    def __init__(self):
        self.magic = MagicMax(52, 5)
        self.cm = CardMapper()

    def check_card(self, cards: list, card_num: int = 5) -> str:
        """
        验证卡面是否符合以下条件：
        - 包含 card_num 个卡面
        - 每个卡面都由合法的花色和数字组成
        - 每个卡面各不相同
        """

        # 检查列表长度是否合法
        if len(cards) != card_num:
            return f"提示：当前牌组长度为{len(cards)}，请输入 {card_num} 张卡面"

        # 检查卡面是否符合要求
        for card in cards:
            if not self.cm.is_card(card):
                return f"提示：卡面 {card} 解析失败"

        # 检查是否有重复元素
        if len(set(cards)) != len(cards):
            return "提示：牌组中存在重复卡面"

        # 验证通过：列表符合所有条件
        return "pass"

    def im_feeling_lucky(self):
        """随机抽取 5 张牌"""
        return self.cm.random_n_cards(5)

    def chico(self, cards: list):
        """Chico 编码卡组"""
        # 将卡面解析为数字编码
        parsed_list = [self.cm.card_to_num(e) for e in cards]

        first_four, fifth_card = self.magic.reverse(self.magic.encoder(parsed_list))

        # 将数字编码转换为卡面
        first_four_str = ' '.join([self.cm.num_to_card(e) for e in first_four])
        fifth_card_str = self.cm.num_to_card(fifth_card)

        return (
            "五张扑克牌被 Chico 分为两堆：\n"
            f"- 前四张牌：{first_four_str}\n"
            f"- 第五张牌：{fifth_card_str}\n"
            "把前4张牌告诉 Dico 吧！他可以据此猜出第5张"
        )

    def dico(self, cards: list):
        """dico 解码牌组"""
        # 将卡面解析为数字编码
        parsed_list = [self.cm.card_to_num(e) for e in cards]

        fifth_card = self.magic.decoder(parsed_list)

        # 将数字编码转换为卡面
        fifth_card_str = self.cm.num_to_card(fifth_card)

        return f"第五张扑克牌是 {fifth_card_str}"
