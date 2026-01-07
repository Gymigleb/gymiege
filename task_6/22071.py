from turtle import *

tracer(0)

screensize(4000, 4000)

sc = 10

forward(30*sc)
left(60)
forward(24*sc)
right(240)

forward(54*sc)
left(120)
forward(24*sc)
left(60)

up()

forward(sc*30)
right(90)
forward(sc*20)
left(90)

down()

for i in range(17):
    forward(6*sc)
    left(90)
    forward(80*sc)
    left(90)

up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*sc,y*sc)
        dot(3,"red")
print((7-1) + (11-1) + (22-1) + (7-1) * 2)
update()
done()
