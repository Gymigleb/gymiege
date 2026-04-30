from turtle import *

tracer(0)
sc = 5
screensize(4000, 4000)

for i in range(7):
    fd(18*sc)
    right(90)
    fd(28*sc)
    right(90)

up()
fd(3*sc)
right(90)
fd(5*sc)
left(90)
down()

for i in range(7):
    fd(250*sc)
    rt(90)
    fd(402*sc)
    rt(90)

up()
# for x in range(-405, 405):
#     for y in range(-405, 405):
#         goto(x*sc, y*sc)
#         dot(3, "red")

print(251*403 + 19*29 - 24*16)

update()
done()