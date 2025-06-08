from itertools import permutations

sheet = '21 32 42 54 61 62 72 73 74 82 85 86'
sheet = sheet + ' ' + sheet[::-1]
graph = 'АВ АГ ГБ БД ВГ ГД ВЕ ЕГ ГИ ДИ ЕЖ ЖИ'
graph = graph + ' ' + graph[::-1]

unip = set(graph.replace(' ', ''))
for permutation in permutations(unip):
    cache = sheet
    for index, point in enumerate(permutation):
        cache = cache.replace(str(index + 1), point)
    if set(graph.split()) == set(cache.split()):
        print(permutation)