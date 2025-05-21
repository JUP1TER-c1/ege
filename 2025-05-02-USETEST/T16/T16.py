from functools import lru_cache


@lru_cache(None)
def F(n):
    if n <= 5:
        return 1
    return n + F(n - 2)

for i in range(1, 2200):
    F(i)

print(F(2126) - F(2122))