from itertools import permutations, product
from infEGE import *

def F(x, y, w, z):
    return (w <= (not (z <= x))) or y

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, a1, a2, a3), (0, 1, 0, a4), (a5, 0, a6, a7)]
    for permutation in permutations("xywz"):
        if [F(**dict(zip(permutation, row))) for row in table] == [0, 0, 0]:
            print(permutation)

print_true_table('xywz', '(w -> (~(z -> x)))|y', 0)