from itertools import product, repeat, permutations

def F(x, y, z, w):
    return (z == (x <= w)) and (x != (w <= y))

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, a1, 0, 0), (a2, a3, 0, 0), (1, 1, a4, 0)]
    if len(table) != len(set(table)): continue
    for permutation in permutations('xyzw'):
        if [F(**dict(zip(permutation, row))) for row in table] == [1, 1, 0]:
            print(permutation)
