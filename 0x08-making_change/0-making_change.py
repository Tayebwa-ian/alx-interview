#!/usr/bin/python3
"""
Minimum Coins Algorithm
"""


def makeChange(coins: list, total: int) -> int:
    """
    determine the fewest number of coins needed to meet a given amount total
    Args:
        coins: a list of avaliable coins
        total: the amount to change
    """
    num_of_min_coins = 0
    if total > 0:
        # sort and reverse the list of coins
        coins = sorted(coins)[::-1]
        for coin in coins:
            while coin <= total:
                num_of_min_coins += 1
                total -= coin
            if total == 0:
                return num_of_min_coins
    return -1
