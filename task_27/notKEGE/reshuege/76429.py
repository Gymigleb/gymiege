from math import dist
from turtle import *

def sum_l(sA, kl):
    out = 0
    for sB in kl:
        out += dist(sA, sB)
    return out

def cent(kl):
    min_l = 10**100
    cent_star = [0, 0]
    for sA in kl:
        l = sum_l(sA, kl)
        if min_l >= l:
            min_l = l
            cent_star = sA
    return cent_star

def draw(kl, sc, color, dot_size):
    up()
    for star in kl:
        goto(star[0]*sc, star[1]*sc)
        dot(dot_size, color)

def A():
    f = open("76429A.txt")
    KL = [[], []]
    sc = 50
    tracer(0)
    screensize(4000, 4000)
    for i in range(209):
        x, y = map(float, f.readline().split())
        KL[0 if y < 15 else 1].append((x, y))
    centers = []
    centers.append((cent(KL[0])))
    centers.append((cent(KL[1])))
    draw(KL[0], sc, "red", 3)
    draw(KL[1], sc, "blue", 3)
    draw(centers, sc, "yellow", 5)
    print(centers)
    print(int((centers[0][0] + centers[1][0])/2*10000))
    print(int((centers[0][1] + centers[1][1])/2*10000))
    # update()
    # done()

def B():
    f = open("76429B.txt")
    KL = [[], [], []]
    sc = 50
    tracer(0)
    screensize(4000, 4000)
    for i in range(509):
        x, y = map(float, f.readline().split())
        KL[0 if x < -5 else 
        1 if x < 7 else
        2].append((x, y))
    centers = []
    centers.append((cent(KL[0])))
    centers.append((cent(KL[1])))
    centers.append((cent(KL[2])))
    draw(KL[0], sc, "red", 5)
    draw(KL[1], sc, "blue", 5)
    draw(KL[2], sc, "green", 5)
    draw(centers, sc, "yellow", 15)
    print(centers)
    print(int((centers[0][0] + centers[1][0] + centers[2][0])/3*10000))
    print(int((centers[0][1] + centers[1][1] + centers[2][1])/3*10000))
    # update()
    # done()


# A()
B()

update()
done()