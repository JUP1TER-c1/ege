from itertools import permutations

graph = "АБ АВ АГ БА БГ БД ВА ВЕ ГА ГБ ГД ГЕ ДВ ДГ ДК ЕВ ЕГ ЕЛ КД КЛ ЛЕ ЛК"
sheet = "12 14 18 21 23 32 36 38 41 47 56 57 58 63 65 68 74 75 81 83 85 86"

unique_endpoints = set(graph.replace(" ", ""))
for permutation in permutations(unique_endpoints):
    cache = graph
    for index, endpoint in enumerate(permutation):
        cache = cache.replace(endpoint, str(index + 1))
    if set(cache.split()) == set(sheet.split()):
        print(permutation)