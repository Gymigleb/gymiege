from itertools import *

def t(a):
    a = list(a)
    for i in range(0, 20, 2):
        for j in range(len(a)):
            if a[j] == i: a[j] = 0
    for i in range(1, 20, 2):
        for j in range(len(a)):
            if a[j] == i: a[j] = 1
    a = map(str, a)
    a = "".join(a)
    return "00" not in a and "11" not in a

cnt = 0

for i in product(range(20), repeat=5):
    if t(i) and i[0] + i[-1] == 26: cnt += 1
    # if cnt != 0 and cnt % 10000: print(cnt)

print(cnt)