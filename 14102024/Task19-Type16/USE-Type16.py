import sys
sys.setrecursionlimit(1000000)
def F(n):
    if n < 11:
        return 10
    else:
        return n + F(n - 1)
print(F(2204) - F(2202))