from math import floor


def euclid_distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def chebyshev_distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def locate_centroid_euclid(cluster):
    min_dist_sum = 10**20
    centroid = []
    for candidate in cluster:
        dist_sum = sum(euclid_distance(candidate, point) for point in cluster)
    if dist_sum <= min_dist_sum:
        min_dist_sum = dist_sum
        centroid = candidate
    return candidate

def locate_centroid_chebyshev(cluster):
    min_dist_sum = 10**20
    centroid = []
    for candidate in cluster:
        dist_sum = sum(chebyshev_distance(candidate, point) for point in cluster)
    if dist_sum <= min_dist_sum:
        min_dist_sum = dist_sum
        centroid = candidate
    return candidate
# A
clusters = [[], []]
for line in open('27A.txt'):
    point = list(map(float, line.split()))
    if point[0] > 7:
        clusters[0].append(point)
    else:
        clusters[1].append(point)

centroid_distances = []
for cluster in clusters:
    print(locate_centroid_chebyshev(cluster))
    print(locate_centroid_euclid(cluster))
    centroid_distances.append(floor(euclid_distance(locate_centroid_euclid(cluster), locate_centroid_chebyshev(cluster))*10000))

print(centroid_distances)

# B
clusters = [[], [], []]
for line in open('27B.txt'):
    point = list(map(float, line.split()))
    if point[0] < -0.375:
        clusters[0].append(point)
    elif point[1] > 4.75:
        clusters[1].append(point)
    else:
        clusters[2].append(point)

centroid_distances = []
for cluster in clusters:
    print(locate_centroid_chebyshev(cluster))
    print(locate_centroid_euclid(cluster))
    centroid_distances.append(floor(euclid_distance(locate_centroid_euclid(cluster), locate_centroid_chebyshev(cluster))*10000))

print(centroid_distances)

