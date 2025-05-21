def F(n):
    if n <= 2:
        return 1
    else:
        return F(n - 2) * (n - 1)

print(F(8))