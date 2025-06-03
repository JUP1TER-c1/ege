def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def locate_centroid(cluster):
    min_dist_sum = 10**10
    centroid = []
    for candidate in cluster:
        dist_sum = sum(distance(candidate, point) for point in cluster)
        if dist_sum < min_dist_sum:
            centroid = candidate
            min_dist_sum = dist_sum
    return centroid

# A
clusters = [[], []]
for point in open('A.txt'):
    point = list(map(float, point.split()))
    if point[1] > -2:
        clusters[0].append(point)
    if point[1] < -2:
        clusters[1].append(point)

centroids = [locate_centroid(cluster) for cluster in clusters]
print(sum(centroid[0] for centroid in centroids)*10000/len(centroids))
print(sum(centroid[1] for centroid in centroids)*10000/len(centroids))

# B
clusters = [[], [], []]
for point in open('B.txt'):
    point = list(map(float, point.split()))
    if point[1] < 0:
        clusters[0].append(point)
    elif point[0] > -6 and point[1] > 0:
        clusters[1].append(point)
    else:
        clusters[2].append(point)

centroids = [locate_centroid(cluster) for cluster in clusters]
print(abs(sum(centroid[0] for centroid in centroids)*10000/len(centroids)))
print(abs(sum(centroid[1] for centroid in centroids)*10000/len(centroids)))