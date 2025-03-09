from itertools import product, permutations


def f(x, y, z, w):
    return (x and not y) or (y == z) or not w

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, a1, a2, 0), (0, 1, 0, 1), (a3, 1, 0, a4)]
    if len(set(table)) != len(table): continue
    for permutation in permutations('xyzw'):
        if [f(**dict(zip(permutation, row))) for row in table] == [0,0,0]:
            print(permutation)
