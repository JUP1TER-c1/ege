from itertools import permutations

graph_literal_roads   = "АБ АВ АГ АИ БА БВ ВА ВБ ВК ГА ГД ГЕ ДГ ДЖ ЕГ ЕЖ ЕИ ЖД ЖЕ ЖК ИА ИЕ ИК КВ КЖ КИ"
sheet_numerical_roads = "16 19 23 25 27 32 34 39 43 46 47 52 58 61 64 68 69 72 74 78 85 86 87 91 93 96"

unique_endpoints = set(graph_literal_roads.replace(' ', ''))
for permutation in permutations(unique_endpoints):
    graph_numerical_roads = graph_literal_roads
    for index, endpoint in enumerate(permutation):
        graph_numerical_roads = graph_numerical_roads.replace(endpoint, str(index + 1))
    if set(sheet_numerical_roads.split()) == set(graph_numerical_roads.split()):
        print(permutation)