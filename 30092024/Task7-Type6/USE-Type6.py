from turtle import *
left(90)
tracer(0)
screensize(2000,2000)
size=30
down()
for i in range(3):
    forward(7 * size)
    right(90)
forward(8 * size)
for i in range(3):
    left(90)
    forward(5 * size)
up()
for x in range(-1, 8):
    for y in range(-5, 8):
        goto(x * size, y * size)
        dot(1*(size//5), 'red')
done()