def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def locate_centroid(cluster):
    minimal_distance_sum = 10**40
    result = []
    for candidate in cluster:
        distance_sum = sum(distance(point, candidate) for point in cluster)
        if distance_sum < minimal_distance_sum:
            minimal_distance_sum = distance_sum
            result = candidate

    return result

# file = open("27.13.A_19567.txt")
# clusters = [[],[]]
# for line in file:
#     x, y = map(float, line.split())
#     if (-1 < x < 2) and (-4 < y < -1):
#         clusters[0].append([x, y])
#     elif (1 < x < 5) and (0 < y < 2):
#         clusters[1].append([x, y])

file = open("27.13.B_19567.txt")
clusters = [[],[],[],[],[],[]]

cord_xs = []
cord_ys = []
for cluster in clusters:
    centroid = locate_centroid(cluster)
    cord_xs.append(centroid[0])
    cord_ys.append(centroid[1])

print((sum(cord_xs)/len(cord_xs))*10_000)
print((sum(cord_ys)/len(cord_ys))*10_000)