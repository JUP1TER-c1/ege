from itertools import permutations

sheet = '41 43 51 52 53 62 64 71 72 76'
sheet = sheet + ' ' + sheet[::-1]
graph = 'AB AD AF FD BC BG DC FE EC EG'
graph = graph + ' ' + graph[::-1]

unip = set(graph.replace(' ', ''))
for permutation in permutations(unip):
    cache = sheet
    for index, point in enumerate(permutation):
        cache = cache.replace(str(index + 1), point)
    if set(cache.split()) == set(graph.split()):
        print(permutation)