from itertools import permutations

sheet = '12 13 17 21 23 26 31 32 34 43 46 57 58 62 64 68 71 75 78 85 86 87'
graph = 'AB AC AF BA BG BH CA CD CF DC DE DG ED EG FA FC FH GB GD GE HB HF'

uni = set(graph.replace(" ", ""))
for permutation in permutations(uni):
    cache = sheet
    for index, endpoint in enumerate(permutation):
        cache = cache.replace(str(index+1), endpoint)
    if set(graph.split()) == set(cache.split()):
        print(permutation)