from itertools import permutations

sheet = "21 42 43 53 61 63 72 74 75"
sheet = sheet + " " + sheet[::-1]
graph = "BG BD GF GC DE FC FE CA EA"
graph = graph + " " + graph[::-1]

unique_endpoints = set(graph.replace(" ", ""))
for permutation in permutations(unique_endpoints):
    cache = sheet
    for index, point in enumerate(permutation):
        cache = cache.replace(str(index + 1), point)
    if set(cache.split()) == set(graph.split()):
        print(permutation)
