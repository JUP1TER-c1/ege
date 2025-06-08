def formula(x, A):
    return ((x&45 > 0) or (x&89 > 0)) <= (x&A > 0)

for A in range(1000):
    if all([formula(x, A) for x in range(10000)]):
        print(A)
        break