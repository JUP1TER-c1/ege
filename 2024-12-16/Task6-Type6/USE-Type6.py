from turtle import *

scale = 30
screensize(2560, 1440)
tracer(0)
for i in range(5):
    setheading(180)
    circle(-5*scale, 180)
    setheading(90)
    circle(-5*scale, 180)
    setheading(0)
    circle(-5*scale, 180)
    setheading(270)
    circle(-5*scale, 180)

up()
for i in range(-30, 30):
    for j in range(-30, 30):
        setpos(i*scale, j*scale)
        dot(3, "red")

done()