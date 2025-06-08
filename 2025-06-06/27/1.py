def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def locate_centroid(cluster):
    centroid = []
    min_dist_sum = 10**40
    for candidate in cluster:
        dist_sum = sum([distance(candidate, point) for point in cluster])
        if dist_sum < min_dist_sum:
            centroid = candidate
            min_dist_sum = dist_sum
    return centroid

#A
clusters = [[], []]
for line in open('1.txt'):
    point = list(map(float, line.split()))
    if point[1] > 15:
        clusters[0].append(point)
    else:
        clusters[1].append(point)

centroids = [locate_centroid(cluster) for cluster in clusters]
centrox = [centroid[0] for centroid in centroids]
centroy = [centroid[1] for centroid in centroids]
print((abs(sum(centrox))/len(centrox)) * 10000)
print((abs(sum(centroy))/len(centroy)) * 10000)

#B
clusters = [[], [], []]
for line in open('2.txt'):
    point = list(map(float, line.split()))
    if point[1] < 0:
        clusters[0].append(point)
    elif point[0] > 0:
        clusters[1].append(point)
    else:
        clusters[2].append(point)

centroids = [locate_centroid(cluster) for cluster in clusters]
centrox = [centroid[0] for centroid in centroids]
centroy = [centroid[1] for centroid in centroids]
print((abs(sum(centrox))/len(centrox)) * 10000)
print((abs(sum(centroy))/len(centroy)) * 10000)