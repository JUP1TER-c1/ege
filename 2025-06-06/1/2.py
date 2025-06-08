from itertools import permutations

sheet = '31 43 52 63 64 75 76 81 82 87'
sheet = sheet + ' ' + sheet[::-1]
graph = 'DE DB EB EA BG AH HG HC GF CF'
graph = graph + ' ' + graph[::-1]

unip = set(graph.replace(' ', ''))
for permutation in permutations(unip):
    cache = sheet
    for index, point in enumerate(permutation):
        cache = cache.replace(str(index + 1), point)
    if set(graph.split()) == set(cache.split()):
        print(permutation)