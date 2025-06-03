from itertools import permutations, product


def F(x, y, z, w):
    return not (x <= y) or (z == w) or z


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    tab = [(0, 0, a1, a2), (a3, a4, 1, a5), (a6, 1, 0, a7)]
    for permutation in permutations('xyzw'):
        if [F(**dict(zip(permutation, row))) for row in tab] == [0, 0, 0]:
            print(permutation)

