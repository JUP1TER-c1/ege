from turtle import *
lt(90)
size=30
screensize(2000,2000)
tracer(0)
down()
for i in range(6):
    fd(10*size)
    rt(60)
up()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*size,y*size)
        dot(4,'red')
#Прямоугольник 17*11
setpos(1*size, 0)
down()
fd(10*size)
rt(90)
fd(16*size)
rt(90)
fd(10*size)
rt(90)
fd(16*size)
rt(90)
up()
#Прямоугольник 3*7
setpos(6*size, -3*size)
down()
fd(2*size)
rt(90)
fd(6*size)
rt(90)
fd(2*size)
rt(90)
fd(6*size)
rt(90)
up()
#Прямоугольник 3*7
setpos(6*size, 11*size)
down()
fd(2*size)
rt(90)
fd(6*size)
rt(90)
fd(2*size)
rt(90)
fd(6*size)
up()
done()

#28 свободных + 42 из двух прямоугольников 3*7 + 187 прямоугольник 11*17 + 11 на границе