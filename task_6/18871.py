from turtle import *

sc = 10
tracer(0)

for i in range(2):
    fd(sc*10)
    right(90)
    fd(sc*20)
    rt(90)

up()
bk(sc*4)
rt(90)
fd(sc*7)
left(90)
down()

for i in range(4):
    fd(sc*8)
    lt(90)
    fd(sc*12)
    lt(90)

up()
fd(sc*10)
down()

for i in range(4):
    fd(sc*12)
    right(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(sc*x, sc*y)
        dot(3, "red")

print(13*13 + 11*21 - 5*13)
update()
done()