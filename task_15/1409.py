from itertools import *

p = list(range(2, 22, 2))
q = list(range(3, 30, 3))
r = list(range(12, 61, 12))

l = [x + e for x in range(2, 61) for e in (0, 0.1, 0.9)]

def f(x):
    P = x in p
    Q = x in q
    R = x in r
    A = not (s <= x <= e)
    return A <= ((P and Q) <= R)

def proizv(s, e):
    out = 1
    for i in range(round(s), round(e) +1):
        out *= i
    return out

ans = []

for s, e in combinations(l, 2):
    for x in l:
        if  not(f(x)):
            ans.append(proizv(s, e))
        
print(min(ans))
print(6*18)