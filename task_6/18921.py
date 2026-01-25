from turtle import *

sc = 10
tracer(0)

for i in range(13):
    fd(sc*13)
    right(90)
    fd(sc*5)

up()
right(90)
fd(sc*7)
left(90)
fd(sc*10)
down()

for i in range(23):
    fd(sc*8)
    left(90)
    fd(sc*11)
    left(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*sc, y*sc)
        dot(3, "red")

print(18*18 + 8*11 - 3*7)
done()