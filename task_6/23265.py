from turtle import *

tracer(0)

sc = 10

for i in range(2):
    forward(20*sc)
    left(270)
    backward(12*sc)
    right(90)

up()

forward(sc*9)
right(90)
forward(sc*7)
left(90)

down()

for i in range(2):
    forward(13*sc)
    right(90)
    forward(6*sc)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3,"red")
update()
done()