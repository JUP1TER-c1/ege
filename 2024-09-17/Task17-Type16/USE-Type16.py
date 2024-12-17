def F(n):
    if n < 3:
        return 1
    else:
        return sum(F(i) for i in range(1, n))

print(F(18))