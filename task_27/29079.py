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
    with open("./files/27_A_29079.txt") as f:
        for i in f:
            x, y, t = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if t[0] == "N" and t[2:] == "IV":
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

    # print([len(CL) for CL in TSS]) # [2, 2]

    A1 = min(dist(centers[0], stB) for stB in TSS[1])
    A1 = min([A1] + [dist(centers[1], stB) for stB in TSS[0]])
    A2 = max(dist(centers[0], stB) for stB in TSS[1])
    A2 = max([A1] + [dist(centers[1], stB) for stB in TSS[0]])

    print(int(A1*10_000), int(A2*10_000))

def B():
    data = []
    TS = []
    with open("./files/27_B_29079.txt") as f:
        for i in f:
            x, y, t = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if t[0] == "J" and t[2:] == "V":
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
    # print([len(CL) for CL in TSS]) # [8, 1, 2]

    B1 = max(stA[0] for stA in TSS[0])
    B2 = max(stA[1] for stA in TSS[2])
    
    print(int(B1*10_000), int(B2*10_000))


A()
B()