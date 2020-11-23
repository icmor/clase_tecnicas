''' Recursive Factorial '''
from wrapper import high_limit


def recur_factorial(x):
    if x < 2:
        return 1
    return x * recur_factorial(x - 1)


factorial = high_limit(recur_factorial, "factoriales.txt")
