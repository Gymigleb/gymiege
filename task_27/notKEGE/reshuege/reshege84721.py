from random import *
from turtle import *
from math import dist

tracer(0)
screensize(5000, 5000)
sc = 40

def sum_l(a, kl):
    s = 0
    for b in kl:
        s += dist(a, b)
    return s

def max_l(kl):
    max_dist = 0
    d_pA = [0, 0]
    d_pB = [0, 0]
    for pA in kl:
        for pB in kl:
            now_d = dist(pA, pB)
            if now_d > max_dist:
                d_pA = pA
                d_pB = pB
                max_dist = now_d
    return d_pA, d_pB, max_dist

def center(kl):
    min_s = 10**100
    for p in kl:
        s = sum_l(p, kl)
        if s < min_s:
            min_s = s
            min_p = p
    return min_p

def B():
    KL = [[], [], [], []]


    for s in open("27B.txt"):
        x, y = p = [float(e) for e in s.split()]
        KL[1 if y > 25 else
        2 if y < 0 else
        3 if y < 10 and x < 0 else
        0].append(p) 

    up()
    centers = []

    for kl, clr in zip(KL, ["red", "blue", "green", "purple"]):
        for p in kl:
            goto(p[0]*sc, p[1]*sc)
            dot(10, clr)
        update()
        centers.append(center(kl))
        print(clr, len(kl), p)
        goto(centers[-1][0]*sc, centers[-1][1]*sc)
        dot(20, "yellow")

    max_diam = max_l(KL[3])[2]
    print("max_diam", int(max_diam* 10000))

    diam_dots = []
    for kl in KL[1:]:
        pA, pB, diam = max_l(kl)
        diam_dots += [pA, pB]
        up()
        goto(pA[0]*sc, pA[1]*sc)
        down()
        dot(10, "black")
        goto(pB[0]*sc, pB[1]*sc)
        dot(10, "black")
    print("Qw2", int(max_l(diam_dots)[2]*10000))
    done()

def A():
    KL = [[], []]
    for i in open("27A.txt"):
        x, y = map(float, i.split())
        KL[0 if x < 15 else 1].append((x, y))
    sc = 40

    up()
    for kl, clr in zip(KL, ["red", "blue"]):
        for p in kl:
            goto(p[0]*sc, p[1]*sc)
            dot(10, clr)
        update()
        print(clr, len(kl))

    diam_dots = []
    for kl in KL:
        pA, pB, diam = max_l(kl)
        diam_dots += [pA, pB]
        up()
        goto(pA[0]*sc, pA[1]*sc)
        down()
        dot(10, "black")
        goto(pB[0]*sc, pB[1]*sc)
        dot(10, "black")
    
    diam_dots.sort(reverse=True)
    print(diam_dots)
    print("px", int((diam_dots[0][0] + diam_dots[1][0]) * 10000))
    diam_dots.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(diam_dots)
    print("py", int((diam_dots[0][1] + diam_dots[1][1]) * 10000))

    done()


A()