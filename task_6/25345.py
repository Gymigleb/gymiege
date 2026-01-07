from turtle import *

sc = 10
tracer(0)

for i in range(6):
    fd(sc * 33)
    right(90)
    fd(sc * 20)
    right(90)

up()
fd(sc * 3)
right(90)
fd(sc * 9)
left(90)
down()

for i in range(6):
    fd(sc * 24)
    right(90)
    fd(sc * 25)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3,"red")

update()
done()