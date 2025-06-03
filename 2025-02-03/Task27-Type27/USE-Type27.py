from idlelib.squeezer import count_lines_with_wrapping


def distance(p1, p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5

def locate_centroid(cluster):
    min_distance_summ = float('inf')
    result = []
    for candidate in cluster:
        distance_summ = sum(distance(candidate, point) for point in cluster)
        if distance_summ < min_distance_summ:
            min_distance_summ = distance_summ
            result = candidate
    return result

def line(point0, point1, x):
    x0 = point0[0]
    y0 = point0[1]
    x1 = point1[0]
    y1 = point1[1]
    # (x-x0)/(x1-x0) = (y-y0)/(y1-y0)
    # (x-x0)(y1-y0)/(x1-x0) = y - y0
    # y = (x-x0)(y1-y0)/(x1-x0) + y0
    return (x-x0)(y1-y0)/(x1-x0) + y0
def in_circle(center, radius, point):
    return not distance(center, point) > radius

# clusters = [[], []]
# for line in open('demo_2025_27_А.txt'):
#     line = line.split()
#     line[0] = float(line[0].replace(',', '.'))
#     line[1] = float(line[1].replace(',', '.'))
#     for x, y in [line]:
#         if y > 5:
#             clusters[0].append([x, y])
#         else:
#             clusters[1].append([x, y])

clusters = [[], [], []]
for line in open('demo_2025_27_Б.txt'):
    line = line.split()
    line[0] = float(line[0].replace(',', '.'))
    line[1] = float(line[1].replace(',', '.'))
    for x, y in [line]:
        if in_circle([1.23, 1.17], 2, [x, y]):
            clusters[0].append([x, y])
        if in_circle([6.69, 5.32], 2, [x, y]):
            clusters[1].append([x, y])
        if in_circle([3.32, 8.75], 2, [x, y]):
            clusters[2].append([x, y])

centroid_xs = []
centroid_ys = []
for cluster in clusters:
    centroid = locate_centroid(cluster)
    centroid_xs.append(centroid[0])
    centroid_ys.append(centroid[1])

print(sum(centroid_xs)*10_000/len(centroid_xs))
print(sum(centroid_ys)*10_000/len(centroid_ys))