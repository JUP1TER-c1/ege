from itertools import product, permutations


def f(x, y, z, w):
    return ((z <= w) or (y == w)) and ((x or z) == y)

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, 1, 1, 0), (a1, 1, 0, a2), (0, a3, a4, 1)]
    if len(set(table)) != 3: continue
    for permutation in permutations('xyzw'):
        if [f(**dict(zip(permutation, row))) for row in table] == [1, 1, 1]:
            print(permutation)