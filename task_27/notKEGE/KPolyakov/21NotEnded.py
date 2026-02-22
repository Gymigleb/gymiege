from turtle import *
from math import dist

def draw(kl, sc, dot_size, color):
    up()
    for s in kl:
        goto(s[0]*sc, s[1]*sc)
        dot(dot_size, color)
    update()

def min_l(klA, klB):
    return min([dist(A, B), A, B] for A in klA for B in klB )

def max_l(klA, klB):
    return max([dist(A, B), A, B] for A in klA for B in klB )

def B():
    f = open("./21/B.txt")
    KL = [[], [], [], []]
    for s in f:
        x, y = p = list(map(float, s.replace(",", ".").split()))
        KL[0 if y < 1.5 else
        1 if y < 4.5 and x < 6 else
        2 if x < 5 else
        0 if x < 7 else
        3 if x < 11 else
        0].append(p)

        

    for i, col in zip(KL, ["red", "green", "blue", "pink"]) :
        draw(i, 40, 7, col)
    

    min_d = min_l(KL[1], KL[2])
    draw(min_d[1:], 40, 10, "yellow")
    max_dGP = max_l(KL[1], KL[3])
    draw(max_dGP[1:], 40, 10, "yellow")
    print(max_dGP[0])
    max_dBP = max_l(KL[2], KL[3])
    draw(max_dBP[1:], 40, 10, "yellow")
    print(max_dBP[0])

screensize(2000, 2000)
tracer(0)
B()
done()