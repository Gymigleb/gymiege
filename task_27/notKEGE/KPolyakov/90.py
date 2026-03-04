from turtle import *
from math import *

def draw(kl, sc, color, dot_size):
    up()
    for x, y in kl:
        goto(sc*x, sc*y)
        dot(dot_size, color)
    update()

def sum_dist(kl, stA):
    return sum(dist(stA, stB) for stB in kl)

def cent(kl):
    return min((sum_dist(kl, stA), stA)for stA in kl)

def A():
    KL = [[], [], [], [], []]
    sc = 40
    dt = 10
    for i in open("./90/27-90a.txt"):
        x, y = p = list(map(float, i.replace(",", ".").split()))
        KL[ 0 if x < -7 and -1 <= y <= 1 else
            0 if y > 7 and -1 <= x <= 1 else
            0 if x > 6 and -1 <= y <= 1 else
            0 if y < -7 and -1 <= x <= 1 else
            1 if x > 0 and y > 0 else
            2 if x < 0 and y > 0 else
            3 if x < 0 and y < 0 else
            4 ].append(p)
        
    for color, kl in zip(["red", "blue", "green", "yellow", "pink"], KL):
        draw(kl, sc, color, dt)

    centrs = [[0, 0]]

    for kl in KL[1:]: centrs.append(cent(kl)[1])
    draw(centrs, sc, "black", dt)

    print(centrs)
    Px = int(sum(c[0] for c in centrs[1:])/4*100000)
    Py = int(sum(c[1] for c in centrs[1:])/4*100000)
    print(Px, Py)

def B():
    KL = [[], [], [], [], []]
    sc = 40
    dt = 10
    for i in open("./90/27-90b.txt"):
        x, y = p = list(map(float, i.replace(",", ".").split()))
        KL[ 0 if y > 6 and x < -6 else
            0 if y > 6 and x > 6  else
            0 if y < -6 and x < -6 else
            0 if 5 <= x <= 8 and -8 <= y <= -5 else
            0 if 6 <= x <= 9 and -10 <= y <= -8 else
            1 if y > x and y > -x else
            2 if y > x and y < -x else
            3 if y < x and y < -x else
            4 ].append(p)
        
    for color, kl in zip(["red", "blue", "green", "yellow", "pink"], KL):
        draw(kl, sc, color, dt)

    centrs = [[0, 0]]

    for kl in KL[1:]: centrs.append(cent(kl)[1])
    draw(centrs, sc, "black", dt)

    print(centrs)
    Px = int(sum(c[0] for c in centrs[1:])/4*100000)
    Py = int(sum(c[1] for c in centrs[1:])/4*100000)
    print(Px, Py)

tracer(0)
screensize(4000, 4000)
# A()
B()
done()