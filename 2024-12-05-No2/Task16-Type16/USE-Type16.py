import sys
sys.setrecursionlimit(100500)

def F(n):
    if n >= 2000:
        return 2000
    elif n < 2000 and n%2 == 1:
        return n * F(n+1)
    else:
        return n * (F(n+1)/2)

print(F(1998)/F(2001))