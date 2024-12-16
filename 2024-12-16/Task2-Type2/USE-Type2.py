from itertools import *

def F1(x, y, z, w):
    return (x or not y) <= (w == z)
def F2(x, y, z, w):
    return (x or not y) == (w <= z)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(0, a1, 0, 0), (a2, 1, 1, a3), (a5, 0, 0, 0)]
    if len(table) == len(set(table)):
        for permutation in permutations('xyzw'):
            if [F1(**dict(zip(permutation, option))) for option in table] == [0, 0, a6] \
                and [F2(**dict(zip(permutation, option))) for option in table] == [0, a4, 0]:
                print(permutation)