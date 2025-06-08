def formula(x, Abase):
    A = Abase[0] <= x <= Abase[1]
    P = 7 <= x <= 68
    Q = 23 <= x <= 42
    return (not A) <= ((Q and P) <= A)

minlen = 10**40
for Amin in range(-10, 150):
    for Amax in range(Amin, 151):
        if all([formula(x, [Amin, Amax]) for x in range(-1000, 1000)]):
            minlen = min(Amax - Amin, minlen)
print(minlen)