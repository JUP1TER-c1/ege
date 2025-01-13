from itertools import permutations

graph = "АБ АГ БА БВ ВБ ВГ ВЕ ГА ГВ ГД ГЖ ДГ ДЕ ЕВ ЕД ЕЖ ЕК ЖГ ЖЕ ЖИ ИЖ ИК КЕ КИ"
sheet = "12 14 15 19 21 26 34 35 37 39 41 43 48 51 53 56 62 65 73 78 84 87 91 93"

unique_points = set(graph.replace(' ', ''))
for permutation in permutations(unique_points):
    cache = graph
    for index, point in enumerate(permutation):
        cache = cache.replace(point, str(index + 1))
    if set(cache.split()) == set(sheet.split()):
        for index, point in enumerate(permutation):
            print(f'{index+1}:{point}')
        print()