from math import dist
from turtle import *
tracer(0)


def sum_l(stA, kl):
    out_s = 0
    for stB in kl: out_s += dist(stA, stB)
    return out_s

def center(kl):
    min_st = [0, 0]
    min_l = 10**100
    for st in kl:
        if min_l > sum_l(st, kl):
            min_l = sum_l(st, kl)
            min_st = st
    return min_st

def centers(kl):
    out = []
    arr =[]
    for st in kl: arr.append((sum_l(st, kl), st))
    arr.sort(key=lambda x: x[0])
    min_l = min(arr, key=lambda x: x[0])[0]
    for i in arr:
        if i[0] == min_l: out.append(i[1])
    return out

def draw(kl, sc, dsc, dcol, xm, ym):
    up()
    for x, y in kl:
        goto(sc*(x - xm), sc*(y - ym))
        dot(dsc, dcol)

def klasteriseA():
    with open("./100/27-100a.txt") as file:
        n = 223
        data = []
        for i in range(n):
            x, y = map(float, file.readline().replace(",", ".").split())
            data.append((x, y))
    kl1 = []
    kl2 = []
    for st in data:
        x, y = st
        if x < 6 and y < 9: kl1.append(st)
        else: kl2.append(st)
    return kl1, kl2

def klasteriseB():
    with open("./100/27-100b.txt") as file:
        n = 623
        data = []
        for i in range(n):
            x, y = map(float, file.readline().replace(",", ".").split())
            data.append((x, y))
    # print("B data readed")
    kl1 = []
    kl2 = []
    kl3 = []
    bag = []
    for st in data:
        x, y = st
        if 9 < x < 14 and 10 < y < 20: kl1.append(st)
        elif 12 < x < 18 and 20 < y < 28: kl2.append(st)
        elif 18 < x < 24 and 19 < y < 28: kl3.append(st)
        else: bag.append(st)
    # print("B data klasterised")
    return kl1, kl2, kl3, bag

def drawKlA():            
    klA1, klA2 = klasteriseA()
    cnA1 = center(klA1)
    cnA2 = center(klA2)

    # draw(klA1, 50, 4, "red", 0, +10)
    # draw(klA2, 50,  4, "green", 0, +10)
    # draw([cnA1], 50, 7, "purple", 0, +10)
    # draw([cnA2], 50,  7, "blue", 0, +10)

    print(int(min(cnA1[0], cnA2[0]) * 10000)) # 3.8471735
    print(int(min(cnA1[1], cnA2[1]) * 10000)) # 6.1225014

def max_l(stA, kl):
    return max(dist(stA, stB) for stB in kl)

def drawKlB():            
    klB1, klB2, klB3, bag = klasteriseB()
    # print(len(klB1), len(klB2), len(klB3))
    cnB1 = center(klB1)
    cnB2 = center(klB2)
    cnB3 = center(klB3)

    # draw(klB1, 10, 4, "red", 0, 0)
    # draw(klB2, 10,  4, "green", 0, 0)
    # draw(klB3, 10,  4, "blue", 0, 0)
    # draw(bag, 10,  7, "purple", 0, 0)

    print(int(dist(cnB1, cnB3) * 10000))
    print(int(max(max_l(cnB1, klB1), max_l(cnB2, klB2), max_l(cnB3, klB3)) * 10000))

    # draw([cnB1], 10, 7, "purple", 0, +10)
    # draw([cnB2], 10,  7, "blue", 0, +10)
    # draw(cnB1, 10, 1, "red", 0, 0)
    # draw(cnB2, 10,  1, "green", 0, 0)
    # draw(cnB3, 10,  1, "blue", 0, 0)


drawKlA()
print("########")
drawKlB()

# done()