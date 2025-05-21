from itertools import permutations

sheet = '21 31 53 54 62 74 75 76 82 83 84'
sheet = sheet + ' ' + sheet[::-1]
graph = 'AE AF ED DF EH DB FC BH BG HG CG'
graph = graph + ' ' + graph[::-1]

unip = set(graph.replace(' ', ''))
for permutation in permutations(unip):
    cache = sheet
    for index, endpoint in enumerate(permutation):
        cache = cache.replace(str(index + 1), endpoint)
    if set(cache.split()) == set(graph.split()):
        print(permutation)