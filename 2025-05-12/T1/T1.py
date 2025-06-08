from itertools import permutations

sheet = '21 31 32 41 54 62 65 74 75'
sheet = sheet + ' ' + sheet[::-1]
graph = 'AD AE DB DF EC EG CG BF FG'
graph = graph + ' ' + graph[::-1]

unip = set(graph.replace(' ', ''))
for permutation in permutations(unip):
    cache = sheet
    for index, point in enumerate(permutation):
        cache = cache.replace(str(index + 1), point)
    if set(cache.split()) == set(graph.split()):
        print(permutation)