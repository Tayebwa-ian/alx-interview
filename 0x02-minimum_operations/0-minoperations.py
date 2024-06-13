#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n: int) -> int:
    """Calculate the minimum operations needed to write character H
    n number of times
    Arg:
        n: the of H characters
    """
    num_of_ops = 0
    divisor = 2
    half_of_n = n // 2
    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            num_of_ops += divisor
        elif divisor < half_of_n:
            divisor += 1
        else:
            break
    return num_of_ops
