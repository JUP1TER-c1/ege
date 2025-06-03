from turtle import *

def arc(r, a, b, alpha):
    seth(towards(xcor() + a, ycor() + b))
    right(90)
    circle(radius=r, extent=-alpha)

tracer(0)
scale = 10
left(90)

right(180)
forward(5*scale)
right(90)
forward(50*scale)
right(90)
forward(5*scale)
for i in range(5):
    arc(5*scale, 5*scale, 0, 180)

up()
for i in range(-51, 2):
    for j in range(-20, 20):
        setpos(i*scale, j*scale)
        dot(size=3)

done()