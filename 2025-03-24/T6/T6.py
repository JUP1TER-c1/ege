from turtle import *

tracer(0)
scale = 9
left(90)

right(180)
forward(2*scale)
right(90)
forward(40*scale)
right(90)
forward(2*scale)
for i in range(4):
    circle(-5*scale, 180)
    left(180)
up()
for x in range(-42, 10):
    for y in range(-5, 10):
        setpos(x*scale, y*scale)
        dot(2, 'red')





done()