from turtle import *

sc = 10
tracer(0)
screensize(3000, 3000)

for i in range(3):
    fd(sc*39)
    right(90)
    fd(sc*48)
    rt(90)

up()
fd(sc*27)
rt(90)
fd(sc*24)
lt(90)
down()

for i in range(3):
    fd(sc*29)
    right(90)
    fd(sc*18)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(sc*x, sc*y)
        dot(3, "red")

update()
print(39*48 + (29 - 12)*18)
done()