def formula(x, Abase):
    A = Abase[0] <= x <= Abase[1]
    P = 3 <= x <= 13
    Q = 12 <= x <= 22
    return (A <= P) or Q

maxlen = 0
for Amin in range(-10, 200):
    for Amax in range(Amin, 201):
        if all([formula(x, [Amin, Amax]) for x in range(-1000, 1000)]):
            maxlen = max(Amax - Amin, maxlen)
print(maxlen)