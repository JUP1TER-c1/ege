from itertools import permutations

graph_literal_roads   = "AB AH AE BH BA CE CG CD DC DF EA EG EC FH FG FD GF GE GC HB HA HF"
sheet_numerical_roads = "12 14 17 21 24 28 35 37 38 41 42 46 53 58 64 67 71 73 76 82 83 85"

unique_endpoints = set(graph_literal_roads.replace(' ', ''))
for permutation in permutations(unique_endpoints):
    graph_numerical_roads = graph_literal_roads
    for index, endpoint in enumerate(permutation):
        graph_numerical_roads = graph_numerical_roads.replace(endpoint, str(index + 1))
    if set(sheet_numerical_roads.split()) == set(graph_numerical_roads.split()):
        print(permutation)