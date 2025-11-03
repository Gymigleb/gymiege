from turtle import *

tracer(0)
screensize(1000,1000)
sc = 10

for i in range(2):
    forward(23*sc)
    left(90)
    backward(27*sc)
    left(90)

up()

backward(sc*5)
right(90)
forward(sc*11)
left(90)

down()

for i in range(2):
    forward(26*sc)
    right(90)
    forward(32*sc)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3,"red")

update()
done()