from itertools import product, permutations

def f(x, y, z, w):
    return ((y or z) <= (z and w)) != ((x and z) <= (w or y))


for a1, a2 in product([0, 1], repeat=2):
    tab = [(a1, 1, 1, 1), (0, 0, 0, a2), (1, 1, 0, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [1, 1, 1]:
                print(p)