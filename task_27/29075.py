from math import dist

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
    with open("./files/27_A_29075.txt") as f:
        for i in f:
            x, y, tp = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if tp[2:] == "III":
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

    # print([len(CL) for CL in TSS]) # [12, 22]

    A1 = centers[0][0]
    A2 = centers[1][1]

    print(int(A1*10_000), int(A2*10_000))


def B():
    data = []
    TS = []
    with open("./files/27_B_29075.txt") as f:
        for i in f:
            x, y, tp = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if tp[0] == "J":
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

    # print([len(CL) for CL in TSS]) # [54, 14, 14]

    B1 = 10**100
    B2 = 0
    for CLA in TSS:
        for CLB in TSS:
            if CLA != CLB:
                for stA in CLA:
                    for stB in CLB:
                        B1 = min(B1, dist(stA, stB))
                        B2 = max(B2, dist(stA, stB))

    print(int(B1*10_000), int(B2*10_000))

A()
B()