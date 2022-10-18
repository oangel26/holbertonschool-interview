#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given
    a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    """
    def minOperations(n):
    """
    This is a method that calculates the fewest number of
    operations needed to result in exactly n H characters
    in the file.
    """
    result = 0
    i = 2

    if isinstance(n, int) and n < 2:
        return 0

    while i <= n + 1:
        if n % i == 0:
            result += i
            n //= i
            i = 2
        else:
            i += 1

    return result


if __name__ == "__main__":
    """
    Main code for testing
    """

    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
