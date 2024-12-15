from itertools import permutations

graph_literal_roads   = "AB AC BA BD CA CE CG DB DF DG EC EF FD FE FG GC GD GF"
sheet_numerical_roads = "14 15 17 24 26 35 36 37 41 42 51 53 56 62 63 65 71 73"

unique_endpoints = set(graph_literal_roads.replace(' ', ''))
for permutation in permutations(unique_endpoints):
    graph_numerical_roads = graph_literal_roads
    for index, endpoint in enumerate(permutation):
        graph_numerical_roads = graph_numerical_roads.replace(endpoint, str(index + 1))
    if set(sheet_numerical_roads.split()) == set(graph_numerical_roads.split()):
        print(permutation)