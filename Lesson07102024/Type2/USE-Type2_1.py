from itertools import product, permutations

def f(x, y, z, w):
    return (z and y) or ((x <= z ) == (y <= w))

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    sheet = [(a1, a2, a3, 1), (1, a4, a5, 1), (1, a6, 1, 1)]
    print(sheet, len(sheet), len(set(sheet)))
    if len(sheet) != len(set(sheet)): continue
    for permutation in permutations('xywz'):
        if [f(**dict(zip(permutation, row))) for row in sheet] == [0, 0, 0]:
            print(permutation)



