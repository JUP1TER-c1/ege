from turtle import *

scale = 30
tracer(0)
down()
for i in range(4):
    forward(14*scale)
    right(90)
for i in range(5):
    forward(5*scale)
    right(45)
up()
for x in range(0, 15):
    for y in range(-14, 1):
        goto(x * scale, y * scale)
        dot(1*(scale//5), 'red')
done()