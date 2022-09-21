#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins: list, total: int) -> int:
    """
    Function that  determine the fewest number of coins needed
    to meet a given amount total.
        Returns:
            Fewest number of coins needed to meet total.
            If total is 0 or less, return 0.
            If total cannot be met by any number of coins you have,
            return -1.
    """
    if total <= 0:
        return 0

    new_coins = []
    coins.sort(reverse=True)
    div = 0

    for coin in coins:
        div = total // coin
        total = total % coin
        new_coins.append(div)
    if total != 0:
        return -1
    return sum(new_coins)
