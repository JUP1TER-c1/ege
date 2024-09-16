import matplotlib.pyplot as plt #На ЕГЭ, я так понимаю, не будет этой библиотеки?
import math
import numpy as np

points = [[0, 0]]

RCC = math.pi/180
angle = 45

for i in range(7):
    points.append([points[-1][0] + (5 * math.cos(angle * RCC)), points[-1][1] + (5 * math.sin(angle * RCC))])
    angle -= 45
    points.append([points[-1][0] + (10 * math.cos(angle * RCC)), points[-1][1] + (10 * math.sin(angle * RCC))])
    angle -= 135


pointsX = [points[i][0] for i in range(len(points))]
pointsY = [points[i][1] for i in range(len(points))]

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(pointsX, pointsY)

rawDotsX = [[i for i in range(-1, 15)] for j in range(-1, 5)]
rawDotsY = [[i for j in range(-1, 15)] for i in range(-1, 5)]
dotsX = []
dotsY = []
for i in range(6):
    for j in rawDotsX[i]:
        dotsX.append(j)
for i in range(6):
    for j in rawDotsY[i]:
        dotsY.append(j)

print(dotsX)
print(dotsY)

print(np.shape(dotsX))
ax.scatter(dotsX, dotsY, c='red', s=[4 for i in range(96)])
ax.scatter(pointsX, pointsY, c='green')

ax.xaxis.set_ticks([i for i in range(-1, 15)])
ax.yaxis.set_ticks([i for i in range(-1, 6)])
plt.grid(True)
plt.show()

#Ответ 27