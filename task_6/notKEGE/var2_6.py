from turtle import *

sc = 50
tracer(0)

for i in range(2):
    fd(6*sc)
    lt(270)
    bk(5*sc)
    lt(270)

up()
fd(4*sc); rt(90); bk(2*sc); lt(90)
down()

for i in range(2):
    fd(8*sc)
    rt(90)
    fd(3*sc)
    rt(90)

up()
fd(4*sc); rt(180); bk(2*sc)
down()

for i in range(3):
    fd(6*sc)
    rt(90)
    fd(7*sc)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*sc, y*sc)
        dot(5, "red")
        
print(20 + 42 + 24)
update()
done()