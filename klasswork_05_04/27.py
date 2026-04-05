from math import dist
from turtle import *

def sum_dist(stA, KL):
    return sum(dist(stA, stB) for stB in KL)

def cent(KL):
    return min((sum_dist(stA, KL), stA) for stA in KL)[1]

def draw(KL, color, dot_size, sc):
    up()
    for st in KL:
        x, y = st
        goto(sc*x, sc*y)
        dot(dot_size, color)
    update()

def A():
    with open("./27_A.txt") as f:
        data = [list(map(float, i.replace(",", ".").split())) for i in f]

    tracer(0)
    screensize(3000, 3000)
    KLS = [[],[]]
    list_cols = ["red", "blue"," yellow"]
    dot_size = 3
    scale = 20

    for st in data:
        x, y = st
        KLS[1 if y > 15 else 0].append(st)

    for color, kl in zip(list_cols, KLS): draw(kl, color, dot_size, scale)

    centers=[cent(kl) for kl in KLS]

    draw(centers, "yellow", dot_size+3, scale)

    q1 = min(len(kl) for kl in KLS)
    stQ = [-1.0, 1.3]
    q2 = dist(stQ, centers[0]) + dist(stQ, centers[1])
    q2 = int(q2*10000)

    print(q1, q2)

def B():
    with open("./27_B.txt") as f:
        data = [list(map(float, i.replace(",", ".").split())) for i in f]

    tracer(0)
    screensize(3000, 3000)
    KLS = [[],[], []]
    list_cols = ["red", "blue","green"]
    dot_size = 3
    scale = 20

    for st in data:
        x, y = st
        KLS[2 if y > 20 else\
            1 if x < 24 else 0].append(st)

    for color, kl in zip(list_cols, KLS): draw(kl, color, dot_size, scale)

    centers=[cent(kl) for kl in KLS]

    draw(centers, "yellow", dot_size+3, scale)

    print([len(kl) for kl in KLS]) # 1 middle; 2 max

    q1 = sum(1 for stB in KLS[1] if dist(centers[1], stB) <= 1.6) - 1
    q2 = max(dist(centers[2], stB) for stB in KLS[2])
    q2 = int(q2*10000)

    print(q1, q2)


# A()
B()
done()