from turtle import *

tracer(0)
screensize(4000,4000)
sc = 3

rt(45)
for i in range(10):
    rt(45)
    fd(sc*203)
    rt(45)
up()
bk(sc*40)
rt(45)
down()
for i in range(5):
    fd(sc*20)
    lt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(sc*x, sc*y)
        dot(1, "red")
print((203-2)**2 + (20-2)**2)
done()