from itertools import permutations

graph_literal_roads   = "АБ АГ БА БВ ВБ ВГ ВЕ ГА ГВ ГД ГЖ ДГ ДЕ ЕВ ЕД ЕЖ ЕК ЖГ ЖЕ ЖИ ИЖ ЖК КЕ КИ"
sheet_numerical_roads = "12 14 15 19 21 26 34 35 37 39 41 43 48 51 53 56 62 65 73 78 84 87 91 93"

unique_endpoints = set(graph_literal_roads.replace(' ', ''))
for permutation in permutations(unique_endpoints):
    graph_numerical_roads = graph_literal_roads
    for index, endpoint in enumerate(permutation):
        graph_numerical_roads = graph_numerical_roads.replace(endpoint, str(index + 1))
    if set(sheet_numerical_roads.split()) == set(graph_numerical_roads.split()):
        print(permutation)