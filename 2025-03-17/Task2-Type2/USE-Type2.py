from itertools import product, permutations


def f(x, y, z, w):
    return ((not x or z) == (y and not w)) <= (z and y)

for a1, a2, a3, a4, a5, a6 in product([1, 0], repeat=6):
    table = [(a1, 1, 1, 1), (a2, a3, 1, 1), (a4, a5, 1, a6)]
    if len(set(table)) != len(table): continue
    for permutation in permutations('xyzw'):
        if [f(**dict(zip(permutation, row))) for row in table] == [0, 0, 0]:
            print(permutation)
