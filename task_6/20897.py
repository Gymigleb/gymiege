from turtle import *

sc = 10
tracer(0)

for i in range(9):
    fd(sc*27)
    right(90)
    fd(sc*30)
    right(90)

up()
fd(sc*3)
right(90)
fd(sc*6)
left(90)
down()

for i in range(9):
    fd(sc*77)
    right(90)
    fd(sc*66)
    right(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*sc, y*sc)
        dot(3, "red")
print(24*4)
update()
done()