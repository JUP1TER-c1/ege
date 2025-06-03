def expression(A, x, y):
    return (3*x + 4*y != 60) or ((A >= x) and (A >= y))

for x in range(1000):
    for y in range(1000):
        if not expression(20, x, y):
            print('??')