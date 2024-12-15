from itertools import permutations

graph_literal_roads   = "АБ АВ БА БВ БГ ВА ВБ ВД ГБ ГД ГЕ ДВ ДГ ДЗ ЕГ ЕЗ ЗД ЗЕ"
sheet_numerical_roads = "16 17 25 26 27 34 35 36 43 45 52 53 54 61 62 63 71 72"

unique_endpoints = set(graph_literal_roads.replace(' ', ''))
for permutation in permutations(unique_endpoints):
    graph_numerical_roads = graph_literal_roads
    for index, endpoint in enumerate(permutation):
        graph_numerical_roads = graph_numerical_roads.replace(endpoint, str(index + 1))
    if set(sheet_numerical_roads.split()) == set(graph_numerical_roads.split()):
        print(permutation)