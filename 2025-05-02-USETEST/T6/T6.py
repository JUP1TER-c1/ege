from turtle import *

tracer(0)
size = 30
left(90)

right(30)
down()
for i in range(3):
    right(150)
    forward(6 * size)
    right(30)
    forward(12*size)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*size, y*size)
        dot(6)
done()