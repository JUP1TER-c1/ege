def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = a1 <= x <= a2
    return ((A) and not (Q)) <= (P or Q)

res = []
points = [point for base in (25, 73, 75, 118) for point in (base, base + 0.01, base - 0.01)]
for a1 in points:
    for a2 in points:
        if a2 >= a1 and all(f(x) for x in points):
            res.append(a2-a1)

print(round(max(res)))