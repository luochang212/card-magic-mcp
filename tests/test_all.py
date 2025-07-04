import itertools

from card_magic_mcp.magic import MagicMax


def factorial(n):
    """计算n的阶乘"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def test_all():
    """测试所有牌组"""
    k = 4
    n = factorial(k) + k - 1
    magic = MagicMax(n, k)
    combinations = itertools.combinations(range(1, n+1), k)

    for combo in combinations:
        nums = list(combo)
        first_four, fifth_card = magic.reverse(magic.encoder(nums))
        guess_fifth_card = magic.decoder(first_four)
        assert fifth_card == guess_fifth_card
