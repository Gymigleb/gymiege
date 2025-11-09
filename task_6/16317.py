from turtle import *

tracer(0)
sc = 10

for i in range(2):
    fd(21*sc)
    right(90)
    fd(27*sc)
    right(90)

up()
fd(9*sc)
right(90)
fd(10*sc)
left(90)
down()

for i in range(2):
    fd(86*sc)
    right(90)
    fd(47*sc)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*sc, y*sc)
        dot(3, "red")

print(18*13)
update()
done()