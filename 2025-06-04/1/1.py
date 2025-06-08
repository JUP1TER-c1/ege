from itertools import permutations

sheet = "41 43 51 52 53 62 64 71 72 76"
sheet = sheet + " " + sheet[::-1]
graph = "EF EC EG FA FD CD CB GB AD AB"
graph = graph + " " + graph[::-1]

unique_endpoints = set(graph.replace(" ", ""))
for permutation in permutations(unique_endpoints):
    cache = sheet
    for index, point in enumerate(permutation):
        cache = cache.replace(str(index + 1), point)
    if set(cache.split()) == set(graph.split()):
        print(permutation)