from turtle import *

scale = 30
tracer(0)
left(90)
down()
for i in range(8):
    right(45)
    forward(6*scale)
up()

for i in range(-20, 20):
    for j in range(-20, 20):
        setpos(i*scale, j*scale)
        dot()
done()