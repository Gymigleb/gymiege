from math import dist

def sum_l(stA, KL):
    return sum(dist(stA, stB) for stB in KL)

def center(KL):
    out = []
    for stA in KL:
        sum_dist = sum_l(stA, KL)
        out.append(([sum_dist], stA))
    return min(out)[1]

def A():
    with open("./files/27_A_28766.txt") as f:
        data = []
        TS = []
        for i in f:
            x, y, type = i.replace(",", ".").split()
            data.append(list(map(float, [x, y])))
            if type[0] == "Y" and type[2:].rstrip() == "III":
                TS.append(list(map(float, [x, y])))
    KLS = [[], []]
    for st in data:
        x, y = st
        KLS[0 if y < 10 else 1].append([x, y])

    print([len(KL) for KL in KLS])
    cent = center(KLS[1])

    a1 = min([dist(cent, stB) for stB in TS])
    a2 = max([dist(cent, stB) for stB in TS])
    a1 = int(a1 * 10000)
    a2 = int(a2 * 10000)

    print(a1, a2)

def B():
    with open("./files/27_B_28766.txt") as f:
        data = []
        TS = []
        for i in f:
            x, y, type = i.replace(",", ".").split()
            data.append(list(map(float, [x, y])))
            if type[0] == "Z" and type[2:].rstrip() == "I":
                TS.append(list(map(float, [x, y])))

    KLS = [[], [], []]
    TSS = [[], [], []]

    for st in data:
        x, y = st
        KLS[0 if y < 15 else\
            1 if y < 22 else\
            2].append([x, y])

    for st in TS:
        x, y = st
        TSS[0 if y < 15 else\
            1 if y < 22 else\
            2].append([x, y])

    # print([len(KL) for KL in TSS])

    b1 = min(dist(stA, stB) for stA in TSS[0] for stB in TSS[0] if stA != stB)
    b1 = min([dist(stA, stB) for stA in TSS[2] for stB in TSS[2] if stA != stB] + [b1])

    b2 = dist(center(KLS[0]), center(KLS[1]))

    b1 = int(b1 * 10000)
    b2 = int(b2 * 10000)

    print(b1, b2)

A()
B()

# from itertools import combinations
# from math import dist
#
# def center(cluster):
#     res = []
#     for dot in cluster:
#         sum_dist = sum(dist(dot, d) for d in cluster)
#         res.append([sum_dist, dot])
#     return min(res)[1]
#
# with open(r'.\files\27_B_28766.txt') as file:
#     dots = []
#     target = []
#     for i in file:
#         x, y, data = i.replace(',', '.').split()
#         dots.append(list(map(float, [x, y])))
#         if data[0] == 'Z' and data[2:].strip() == 'I':
#             target.append(list(map(float, [x, y])))
#
# cluster_1 = [
#     [d for d in dots if d[1] < 15],
#     [d for d in target if d[1] < 15]
# ]
#
# cluster_2 = [
#     [d for d in dots if 15 < d[1] < 22],
#     [d for d in target if 15 < d[1] < 22]
# ]
#
# cluster_3 = [
#     [d for d in dots if 22 < d[1]],
#     [d for d in target if 22 < d[1]]
# ]
#
# B1 = 10 ** 10
# clusters = [cluster_1, cluster_2, cluster_3]
# for c in clusters:
#     B1 = min([B1] + [dist(*d) for d in combinations(c[1], 2)])
#
# min_cluster = center(min(clusters, key=lambda x: len(x[1]))[0])
# max_cluster = center(max(clusters, key=lambda x: len(x[1]))[0])
#
# B2 = dist(min_cluster, max_cluster)
#
# print(B1 * 10_000, B2 * 10_000)