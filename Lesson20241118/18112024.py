#72559
from itertools import *
graph_roads = "АБ АВ АГ БА БД БЖ ВА ВГ ВЕ ГА ГВ ГД ДБ ДГ ДЕ ДЖ ЕВ ЕД ЕЖ ЖБ ЖД ЖЕ"
sheet_roads = "13 14 15 23 26 27 31 32 36 37 41 45 46 51 54 57 62 63 64 72 73 75"

unique_endpoints = set(graph_roads.replace(' ', ''))
for permutation in permutations(unique_endpoints):
    cache = sheet_roads
    print(f'Permutation: {permutation}')
    for index, endpoint in enumerate(permutation):
        print(f'{index}:{endpoint}', end=" ")
        cache = cache.replace(str(index + 1), endpoint)
    print(f'\nRoads: {cache}\n')
    if set(graph_roads.split())==set(cache.split()):
        print(cache)
        print(permutation)


