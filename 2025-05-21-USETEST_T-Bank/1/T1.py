from itertools import permutations

sheet = '31 41 42 51 52 53 63 74 76'
sheet = sheet + ' ' + sheet[::-1]
graph = 'FG FB BC CG BD DC GA DE EA'
graph = graph + ' ' + graph[::-1]

unip = set(graph.replace(' ', ''))
for permutation in permutations(unip):
    cache = sheet
    for index, point in enumerate(permutation):
        cache = cache.replace(str(index + 1), point)
    if set(cache.split()) == set(graph.split()):
        print(permutation)