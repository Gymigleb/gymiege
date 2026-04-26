from math import dist

def sum_dist(stA, CL):
    return sum(dist(stA, stB) for stB in CL)

def center(CL):
    out = []
    for stA in CL:
        out.append([stA, sum_dist(stA, CL)])
    return min(out, key=lambda x: x[1])[0]


def A():
    with open("./files/27_A_28946.txt") as f:
        data = [list(map(float, i.replace(",", ".").split())) for i in f]

    CLS = [[], []]
    for st in data:
        x, y = st
        CLS[0 if y < 15 else 1].append(st)

    centers = []
    for CL in CLS: centers.append(center(CL))

    # print([len(CL) for CL in CLS]) # [301, 344]

    A1 = 0
    for st in CLS[1]:
        x, y = st
        if y < centers[1][1]: A1 += 1

    A2 = abs(centers[0][0] - centers[1][0])

    print(A1, int(A2*10_000))

def B():
    with open("./files/27_B_28946.txt") as f:
        data = [list(map(float, i.replace(",", ".").split())) for i in f]

    CLS = [[], [], []]
    for st in data:
        x, y = st
        CLS[0 if x > 24 else\
            1 if y < 20 else\
            2].append(st)

    centers = []
    for CL in CLS: centers.append(center(CL))

    # print([len(CL) for CL in CLS]) # [148, 200, 902]

    mc = centers[0]
    B1 = 0
    a = 1.8/2
    for st in CLS[0]:
        x, y = st
        if mc[0] - a < x < mc[0] + a:
            if mc[1] - a < y < mc[1] + a:
                B1 += 1
    

    B2 = abs(centers[2][1] - centers[1][1])

    print(B1, int(B2*10_000))


A()
B()