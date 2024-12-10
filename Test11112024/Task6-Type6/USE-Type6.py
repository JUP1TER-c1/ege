from turtle import *

scale = 30
screensize(2000,2000)
tracer(0)

down()
for i in range(6):
    fd(13*scale)
    rt(120)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*scale, y*scale)
        dot(3, 'black')

setpos(4*scale, -1*scale)
down()
fd(5*scale)
rt(90)
fd(5*scale)
rt(90)
fd(5*scale)
rt(90)
fd(5*scale)
rt(90)
up()

done()

#36 + 14 + 30