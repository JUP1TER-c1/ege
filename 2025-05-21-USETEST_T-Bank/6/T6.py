from turtle import *

tracer(0)
scale = 30
left(90)
down()
for i in range(12):
    right(60)
    forward(1 * scale)
    right(60)
    forward(1 * scale)
    right(270)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*scale, y*scale)
        dot(4)

done()