''' Recursive fibonacci with memoization '''

from popup import popup
import time
import json
from wrapper import high_limit


def fib(num):
    memo = {0: 1, 1: 1}

    def compute(x):
        if x in memo:
            return memo[x]

        memo[x] = compute(x-1) + compute(x-2)
        return memo[x]

    return compute(num)


fibonacci = high_limit(fib, "fibonacci.txt")
