from turtle import *

tracer(0)

sc = 10

for i in range(2):
    forward(5*sc)
    left(90)
    backward(13*sc)
    left(90)

up()

backward(sc*10)
right(90)
forward(sc*9)
left(90)
down()

for i in range(2):
    forward(11*sc)
    right(90)
    forward(7*sc)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3,"red")
update()
done()