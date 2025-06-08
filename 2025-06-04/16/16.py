import sys
from functools import lru_cache

from infEGE import *
sys.setrecursionlimit(99999)

@cache
def F(n):
    if n == 1:
        return 1
    else:
        return n * F(n-1)

#for i in range(2025):
#    F(i)

print((F(2024) + (F(2023) * 4)) / (F(2022) * 4))