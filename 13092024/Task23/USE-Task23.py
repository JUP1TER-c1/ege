def add1(n):
    return n+1
def add10(n):
    return n+10
def f(n1, n2):
    if n1 > n2:
        return 0
    if n1 == n2:
        return 1
    else:
        return f(add1(n1), n2) + f(add10(n1), n2)

print(f(10, 31))