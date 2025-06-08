def expr(x, Abase):
    A = Abase[0] <= x <= Abase[1]
    P = 17 <= x <= 58
    Q = 29 <= x <= 80

    return (P) <= (((Q) and not (A)) <= (not (P)))

res = 10**40
for Amin in range(1, 100):
    for Amax in range(Amin, 101):
        if all([expr(x, [Amin, Amax]) for x in range(-1000, 1000)]):
            res = min(Amax - Amin, res)
print(res)