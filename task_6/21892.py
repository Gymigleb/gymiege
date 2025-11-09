from turtle import *

tracer(0)
sc = 10

right(90)
for i in range(7):
    right(45)
    fd(11*sc)
    right(45)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*sc, y*sc)
        dot(3, "red")

update()
print(9*2 + 16*2 + 7*9)
done()