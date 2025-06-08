import sys

from infEGE import cache


@cache
def F(n):
    if n > 2024: return n
    else: return n * F(n+1)

sys.setrecursionlimit(99999)
print(F(2022)/F(2024))