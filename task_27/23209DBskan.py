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
    with open("./files/27_A_23209.txt") as f:
        data = [list(map(float, i.replace(",", ".").split())) for i in f]

    eps = 1
    clusters = []
    while data:
        cluster = [data.pop()]
        for stA in cluster:
            for stB in data.copy():
                if dist(stA, stB) < eps:
                    cluster.append(stB)
                    data.remove(stB)
        if len(cluster) > 30:
            clusters.append(cluster)

    # print([len(cluster) for cluster in clusters])

    centers = []
    for cluster in clusters: centers.append(center(cluster))

    px = int(max(st[0] for st in centers) * 10000)
    py = int(max(st[1] for st in centers) * 10000)

    print(px, py)

def B():
    with open("./files/27_B_23209.txt") as f:
        data = [list(map(float, i.replace(",", ".").split())) for i in f]

    eps = 1
    clusters = []
    while data:
        cluster = [data.pop()]
        for stA in cluster:
            for stB in data.copy():
                if dist(stA, stB) < eps:
                    cluster.append(stB)
                    data.remove(stB)
        if len(cluster) > 30:
            clusters.append(cluster)

    # print([len(cluster) for cluster in clusters])

    centers = []
    for cluster in clusters: centers.append(center(cluster))

    qx = int(abs(centers[2][0] - centers[0][0]) * 10000)
    qy = int(abs(centers[2][1] - centers[0][1]) * 10000)

    print(qx, qy)

A()
B()