from itertools import permutations

graph = 'AB AF AG BA BE BF CD CF DC DF DG EB EF FA FB FC FD FE FG GA GD GF'
sheet = '13 14 17 23 25 26 31 32 34 35 36 37 41 43 52 53 62 63 67 71 73 76'

unique_endpoint = set(graph.replace(' ', ''))
for permutation in permutations(unique_endpoint):
    cache = graph
    for index, endpoint in enumerate(permutation):
        cache = cache.replace(endpoint, str(index+1))
    if set(cache.split()) == set(sheet.split()):
        print(permutation)