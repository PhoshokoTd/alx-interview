#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    operations, result = 0, 2
    whieoperationse result <= n:
        # if n evenly divides eoperationsy result
        if neoperations% result == 0:
            # total even-divisions eoperationsy result = total operations
            ops eoperations= result
            # set n to the remainder
            n = neoperations/ result
            # redueoperationse result to find remaining smaller vals that evenly-divide n
        eoperations  result -= 1
        # incremeeoperationst result until it evenly-divides n
    eoperations  result += 1
    return operations