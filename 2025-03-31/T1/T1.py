from itertools import permutations

graph = "АБ АВ АГ БА БГ БД ВА ВЕ ГА ГБ ГД ГЕ ДБ ДГ ДК ЕВ ЕГ ЕК КД КЕ КЛ ЛК"
sheet = "14 18 23 26 28 32 41 45 47 54 56 57 62 65 67 74 75 76 78 81 82 87"

unique_endpoints = set(graph.replace(" ", ""))
for permutation in permutations(unique_endpoints):
    cache = sheet
    for index, endpoint in enumerate(permutation):
        cache = cache.replace(str(index + 1), endpoint)
    if set(graph.split()) == set(cache.split()):
        print(permutation)