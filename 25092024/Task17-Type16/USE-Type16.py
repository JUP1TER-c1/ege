def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n-2) * n

print(f(7))