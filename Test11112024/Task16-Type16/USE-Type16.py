import sys


def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n - 2 + f(n - 1)

sys.setrecursionlimit(1000000)
print(f(2023) - f(2021))