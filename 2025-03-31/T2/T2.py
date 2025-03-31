from itertools import product, permutations


def f(x, y, z, w):
    return ((x <= y) and (y <= w)) or (z == (x or y))

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, a1, a2, 1), (1, a3, a4, a5), (a6, 1, a7, 1)]
    if len(table) != len(set(table)): continue
    for permutation in permutations('xyzw'):
        if [f(**dict(zip(permutation, row))) for row in table] == [0, 0, 0]:
            print(permutation)