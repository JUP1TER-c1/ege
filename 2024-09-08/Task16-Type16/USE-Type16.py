import sys

def F(n):
    if n < 11:
        return n
    else:
        return n + F(n - 1)

sys.setrecursionlimit(100500)

print(F(2024) - F(2021))