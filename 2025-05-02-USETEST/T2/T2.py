from itertools import product, permutations


def F(x, y, z, w):
    return x and (z <= w) and not y

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, a2, 1, a3), (a4, 1, 0, a5), (1, 0, a6, a7)]
    for permutation in permutations('xyzw'):
        if [F(**dict(zip(permutation, row))) for row in table] == [1, 1, 1]:
            print(permutation)