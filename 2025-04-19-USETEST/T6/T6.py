from turtle import *


tracer(0)
left(90)
size = 10
for i in range(2):
    forward(28 * size)
    right(90)
    forward(18*size)
    right(90)
forward(14*size)
right(90)
forward(10*size)
left(90)
for i in range(2):
    forward(30*size)
    right(90)
    forward(7*size)
    right(90)
up()
for x in range(30):
    for y in range(30):
        setpos(x*size, y*size)
        dot(size=4)
done()