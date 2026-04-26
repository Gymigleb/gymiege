from math import dist

def sum_dist(stA, CL):
    return sum(dist(stA, stB) for stB in CL)

def center(CL):
    out = []
    for stA in CL:
        out.append([stA, sum_dist(stA, CL)])
    return min(out, key=lambda x: x[1])[0]

def A():
    data = []
    TS = []
    with open("./files/27_A_29076.txt") as f:
        for i in f:
            x, y, t = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if t[1] == "2":
                TS.append([x, y])

    CLS = [[], []]
    for st in data:
        x, y = st
        CLS[0 if y < 8 else 1].append(st)

    TSS = [[], []]
    for st in TS:
        x, y = st
        TSS[0 if y < 8 else 1].append(st)

    centers = []
    for CL in CLS: centers.append(center(CL))

    print([len(CL) for CL in TSS]) # [18, 9]

    A1 = centers[1][0]
    A2 = centers[0][1]

    print(int(A1*10_000), int(A2*10_000))

def B():
    data = []
    TS = []
    with open("./files/27_B_29076.txt") as f:
        for i in f:
            x, y, t = i.replace(",", ".").split()
            x, y = float(x), float(y)
            data.append([x, y])
            if t[0] == "Y":
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

    # print([len(CL) for CL in TSS]) # [71, 10, 14]

    B1 = dist(centers[1], centers[0])
    B2 = 0
    for i in range(3):
        for st in TSS[i]:
            B2 = max(B2, dist(centers[i], st))

    print(int(B1*10_000), int(B2*10_000))


A()
B()