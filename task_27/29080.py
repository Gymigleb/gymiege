from math import *
from itertools import *

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
    with open("./files/27_A_29080.txt") as f:
        for i in f:
            x, y, t = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if t[0] == "L" and t[1] == "3":
                TS.append([x, y])

    CLS = [[], []]
    for st in data:
        x, y = st
        CLS[0 if y > 8 else 1].append(st)

    centers = []
    for CL in CLS: centers.append(center(CL))

    # print([len(CL) for CL in CLS]) # [92, 131]
    # print([len(CL) for CL in TSS]) # [10, 9]

    A1 = max(dist(centers[0], stB) for stB in TS)
    A2 = max(dist(centers[1], stB) for stB in TS)

    print(int(A1*10_000), int(A2*10_000))

def B():
    data = []
    TS = []
    with open("./files/27_B_29080.txt") as f:
        for i in f:
            x, y, t = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if t[0] == "L":
                TS.append([x, y])

    CLS = [[], [], []]
    for st in data:
        x, y = st
        CLS[0 if x > 22 else\
            1 if y < 22 else\
            2].append(st)

    TSS = [[], [], []]
    for st in TS:
        x, y = st
        TSS[0 if x > 22 else\
            1 if y < 22 else\
            2].append(st)

    centers = []
    for CL in CLS: centers.append(center(CL))

    # print([len(CL) for CL in CLS]) # [451, 100, 74]
    # print([len(CL) for CL in TSS]) # [77, 14, 8]

    B1 = dist(centers[0], centers[2])
    B2 = max(dist(stA, stB) for CLA, CLB in combinations(TSS, 2) for stA in CLA for stB in CLB )

    print(int(B1*10_000), int(B2*10_000))

A()
B()