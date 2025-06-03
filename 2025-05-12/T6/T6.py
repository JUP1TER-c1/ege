from turtle import *

size = 20
left(90)
speed(50)

right(90)
down()
for i in range(7):
    right(45)
    forward(11*size)
    right(45)

tracer(0)
up()
for x in range(-50, 51):
    for y in range(-50, 51):
        setpos(x*size, y*size)
        dot(4)
done()