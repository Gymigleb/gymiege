from turtle import *

tracer(0)
sc = 10

for i in range(8):
    fd(sc*16)
    right(90)
    fd(sc*22)
    right(90)

up()
fd(sc*5)
right(90)
fd(sc*5)
left(90)
down()

for i in range(8):
    fd(sc*52)
    right(90)
    fd(sc*77)
    right(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3, "red")
update()
print(17*23 + 53*79 - 12*18*2)
done()