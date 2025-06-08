import sys

from infEGE import cache


@cache
def F(n):
    if n == 1: return 1
    else: return n * F(n-1)

sys.setrecursionlimit(99999)
print(F(2023)/F(2020))
