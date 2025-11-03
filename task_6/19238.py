from tkinter.constants import RIGHT
from turtle import *

tracer(0)

sc = 10

for i in range(8):
    forward(16*sc)
    right(90)
    backward(22*sc)
    right(90)

up()

forward(sc*16)
right(90)
forward(sc*5)
left(90)
down()

for i in range(8):
    forward(52*sc)
    right(90)
    forward(77*sc)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3,"red")
update()
done()