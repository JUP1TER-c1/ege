def formula(x, y, A):
    return (x + 2*y < A) or (y > x) or (x > 60)

for A in range(1000):
    if all([all([formula(x, y, A) for y in range(1000)]) for x in range(1000)]):
        print(A)
        break