from math import *
from itertools import combinations

def sum_dist(stA, CL):
    return sum(dist(stA, stB) for stB in CL)

def center(CL):
    out = []
    for stA in CL:
        out.append([sum_dist(stA, CL), stA])
    return min(out)[1]

def A():
    data = []
    TS = []
    with open("./files/27_A_29081.txt") as f:
        for i in f:
            x, y, t = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if t[2:] == "VII":
                TS.append([x, y])

    CLS = [[], []]
    for st in data:
        x, y = st
        CLS[0 if y > 8 else 1].append(st)

    TSS = [[], []]
    for st in TS:
        x, y = st
        TSS[0 if y > 8 else 1].append(st)

    centers = []
    for CL in CLS: centers.append(center(CL))

    A1 = 10**100
    A2 = 0
    for i in range(2):
        A1 = min([A1] + [dist(centers[i], stB) for stB in TSS[i]])
        A2 = max([A1] + [dist(centers[i], stB) for stB in TSS[i]])

    # print([len(CL) for CL in TSS])

    print(int(A1*10_000), int(A2*10_000))

def B():
    # data = []
    TS = []
    with open("./files/27_B_29081.txt") as f:
        for i in f:
            x, y, t = i.replace(",", ".").split()
            x, y = float(x), float(y)
            if t[1] >= "8":
                TS.append([x, y])

    TSS = [[], [], []]
    for st in TS:
        x, y = st
        TSS[0 if x > 22 else\
            1 if y < 22 else\
            2].append(st)

    # print([len(CL) for CL in TSS])

    B1 = 10**100
    B2 = 0
    B2cnt = 0
    for CLA, CLB in combinations(TSS, 2):
        for stA in CLA:
            for stB in CLB:
                B1 = min(B1, dist(stA, stB))

    for CL in TSS:
        for stA, stB in combinations(CL, 2):
                B2 += dist(stA,stB)
                B2cnt += 1

    B2 = B2 / B2cnt
    print(int(B1*10_000), int(B2*10_000))

A()
B()