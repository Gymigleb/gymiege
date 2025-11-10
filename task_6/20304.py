from tkinter.constants import RIGHT
from turtle import *

tracer(0)

sc = 10

for i in range(9):
    fd(sc*30)
    right(90)
    fd(12*sc)
    right(90)
up()
left(270)
fd(5*sc)
left(90)
down()

for i in range(2):
    fd(24*sc)
    right(90)
    fd(28*sc)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3,"red")
update()
done()