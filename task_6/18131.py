from turtle import *

tracer(0)
screensize(1000,1000)
sc = 10

for i in range(9):
    fd(22*sc)
    right(90)
    fd(6*sc)
    right(90)

up()
fd(1*sc)
right(90)
fd(5*sc)
left(90)
down()

for i in range(9):
    fd(53*sc)
    right(90)
    fd(75*sc)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3,"red")

update()
done()