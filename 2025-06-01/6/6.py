from turtle import *

scale = 10
speed(1)
left(90)

for i in range(3):
    forward(27*scale)
    right(90)
    forward(12*scale)
    right(90)
up()
forward(4*scale)
right(90)
forward(6*scale)
left(90)
down()
for i in range(4):
    forward(83*scale)
    right(90)
    forward(77*scale)
    right(90)
up()
tracer(0)
for x in range(-20, 40):
    for y in range(-20, 40):
        setpos(x*scale, y*scale)
        dot(4)

done()