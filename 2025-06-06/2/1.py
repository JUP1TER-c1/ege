from itertools import product, permutations


def F(x, y, z, w):
    return (x and (not y)) or (y == z) or w

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tab = [(a1, a2, 1, a3), (1, 0, 0, 0), (1, 0, a4, 1)]
    for permutation in permutations('xyzw'):
        if [F(**dict(zip(permutation, row))) for row in tab] == [0, 0, 0]:
            print(permutation)