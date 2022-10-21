#!/usr/bin/python3
"""
Given a pile of coins of different values, determine
the fewest number of coins needed to meet a given
amount total.
"""


def makeChange(coins, total, acumulated=0, ordered=False):
    """
    Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given
    amount total.
    """
    if len(coins) == 0 and total > 0:
        return -(acumulated + 1)

    if len(coins) == 0:
        return 0

    if not ordered:
        coins.sort(reverse=True)

    biggest, *leftover = coins

    if type(total) is not int or type(biggest) is not int:
        return -1

    if total == 0:
        return 0

    possibleAmount = (total // biggest)

    if possibleAmount == 0:
        return makeChange(leftover, total, acumulated)

    nextTotal = (total % biggest)
    nextChanges = possibleAmount + \
        makeChange(leftover, nextTotal, acumulated + possibleAmount, ordered)
    if nextChanges == -1:
        nextChanges = makeChange(leftover, total, acumulated, ordered)
    return nextChanges


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
    print(makeChange([2, 21], 26))
