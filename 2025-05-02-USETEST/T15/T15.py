def expression(x, y, A):
    return (5 < y) or (x > 32) or (x + 2*y < A)

for A in range(-100, 100):
    if all(expression(x, y, A) for x in range(-100, 101) for y in range(-100, 101)):
        print(A)