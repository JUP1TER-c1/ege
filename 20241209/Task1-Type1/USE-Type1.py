from itertools import permutations


#graph_roads = "AB AG BA BC BD CB CD CE CF CG DB DC DE EC ED EF FC FE FG GA GC GF"
#sheet_roads = "13 14 16 25 27 31 34 35 41 43 45 46 47 52 53 54 61 64 67 72 74 76"
graph_literal_roads = "АБ АГ АЕ БА БВ БГ ВБ ВД ВИ ГА ГБ ГЕ ДВ ДЖ ЕА ЕГ ЕЖ ЖД ЖЕ ЖИ ИВ ИЖ"
sheet_roads = "15 17 18 24 27 28 34 35 37 42 43 47 51 53 56 65 68 71 72 73 74 81 82 86"

unique_endpoints = set(graph_literal_roads.replace(' ', ''))
for permutation in permutations(unique_endpoints):
    graph_numerical_roads = graph_literal_roads
    for index, endpoint in enumerate(permutation):
        graph_numerical_roads = graph_numerical_roads.replace(endpoint, str(index + 1))
    difference = set(sheet_roads.split()) - set(graph_numerical_roads.split())
    if len(difference) == 2:
        print(difference)
