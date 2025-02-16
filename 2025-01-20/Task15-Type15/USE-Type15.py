def f(x, y, A):
    return (x*y < A) or (y > x) or (x >= 8)

for A in range(500):
    count = 0
    for x in range(500):
        for y in range(500):
            if f(x, y, A) == 1:
                count += 1

    if count == 250_000:
        print(A)


