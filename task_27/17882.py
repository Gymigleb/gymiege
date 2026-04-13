from math import dist

def sum_Ls(stA, KL):
    return sum(dist(stA, stB) for stB in KL)

def center(KL):
    min_len = 10**100
    for stA in KL:
        sum_L = sum_Ls(stA, KL)
        if min_len > sum_L:
            min_st = stA
            min_len = sum_L
    return min_st



def A():
    with open("./files/27_A_17882.txt") as f:
        data = [list(map(float, i.split())) for i in f]

    KLS = [[], []]
    for st in data: KLS[0 if st[1] > 3 else 1].append(st)

    centers = []
    for KL in KLS: centers.append(center(KL))

    px = sum(st[0] for st in centers) / 2
    py = sum(st[1] for st in centers) / 2

    print(int(px*10000), int(py*10000))

def B():
    with open("./files/27_B_17882.txt") as f:
        data = [list(map(float, i.split())) for i in f]

    KLS = [[], [], []]
    for st in data:
        x, y = st
        KLS[0 if y < 3.5 else
        1 if x > 5 else 2].append(st)

    centers = []
    for KL in KLS: centers.append(center(KL))

    px = sum(st[0] for st in centers) / 3
    py = sum(st[1] for st in centers) / 3

    print(int(px*10000), int(py*10000))


A()
B()