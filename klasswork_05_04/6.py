from turtle import *

tracer(0)
sc = 10

for i in range(4):
    fd(sc*10)
    right(270)

up()
fd(sc*3)
right(270)
fd(sc*5)
right(90)
down()

for i in range(2):
    fd(sc*10)
    right(270)
    fd(sc*12)
    right(270)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(sc*x, sc*y)
        dot(3, "red")

print(11*11 + 11*13 - 8*6)

update()
done()