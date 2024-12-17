from turtle import *

tracer(0)
scale = 30
left(90)
down()
for i in range(4):
    forward(12*scale)
    right(90)
for i in range(5):
    forward(4*scale)
    right(45)
up()

for i in range(-10, 20):
    for j in range(-10, 20):
        setpos(i*scale, j*scale)
        dot(3, 'red')
done()