from turtle import *

sc = 10
tracer(0)
screensize(2000, 2000)

right(45)
for i in range(3):
    right(45)
    fd(10*sc)
    right(45)

right(315)
fd(10*sc)
right(90)
fd(20*sc)
right(90)

for i in range(2):
    fd(10*sc)
    right(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*sc, y*sc)
        dot(3, "red")

print(8*8*3 + 8*2) # 208
update()
done()