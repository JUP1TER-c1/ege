def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def locate_centroid(cluster):
    minimal_distance_sum = 10**40
    result = []
    for candidate in cluster:
        distance_sum = sum(distance(other, candidate) for other in cluster)
        if distance_sum < minimal_distance_sum:
            minimal_distance_sum = distance_sum
            result = candidate
    return result



file = open("27.21.B_19715.txt")

anomalies = []
# clusters = [[] for _ in range(2)]
# for line in file:                                         #GOURP A
#     x, y = map(float, line.split())
#     if (-1 < x < 1) and (-2 < y < -1):
#         anomalies.append([x, y])
#     if (14 < x < 16) and (5 < y < 4):
#         anomalies.append([x, y])
#     if (11 < x < 12) and (13 < y < 15):
#         anomalies.append([x, y])
#     if (28 < x < 29) and (16 < y < 17):
#         anomalies.append([x, y])
#     if (-2 < x < 12) and (-1 < y < 13):
#         clusters[0].append([x, y])
#     if (14 < x < 28) and (4 < y < 17):
#         clusters[1].append([x, y])
#     if (20 < x < 23) and (5 < y < 4):
#         clusters[1].append([x, y])

clusters = [[] for _ in range(4)]
for line in file:                                         #GOURP B
    x, y = map(float, line.split())
    if (-15 < x < -5) and (-25 < y < -15):
        anomalies.append([x, y])
    elif (95 < x < 105) and (-5 < y < 5):
        anomalies.append([x, y])
    elif (-30 < x < -20) and (-105 < y < -95):
        anomalies.append([x, y])
    elif (-15 < x < -5) and (75 < y < 85):
        anomalies.append([x, y])
    elif (-100 < x < -10) and (-12 < y < 75):
        clusters[0].append([x, y])
    elif (0 < x < 90) and (0 < y < 90):
        clusters[1].append([x, y])
    elif (-95 < x < -5) and (-120 < y < -30):
        clusters[2].append([x, y])
    elif (8 < x < 95) and (-105 < y < -15):
        clusters[3].append([x, y])


cord_xs = []
cord_ys = []
for cluster in clusters:
    centroid = locate_centroid(cluster)
    cord_xs.append(centroid[0])
    cord_ys.append(centroid[1])

print((sum(cord_xs)/len(cord_xs)*10_000))
print((sum(cord_ys)/len(cord_ys)*10_000))