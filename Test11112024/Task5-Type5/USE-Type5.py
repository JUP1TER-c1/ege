def f(n):
    n = bin(n)[2:]

    if int(n, 2) % 5 == 0:
        n += bin(5)[2:]
    else:
        n += '1'

    if int(n, 2) % 7 == 0:
        n += bin(7)[2:]
    else:
        n += '1'

    return int(n, 2)

for i in range(1500000, 1, -1):
    if f(i) < 1728404:
        print(i)
        print(f(i))
        break