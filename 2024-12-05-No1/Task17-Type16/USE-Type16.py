import sys
sys.setrecursionlimit(100500)

def F(n):
    if n < 11:
        return 10
    else:
        return n + F(n-1)

print(F(2024) - F(2020))