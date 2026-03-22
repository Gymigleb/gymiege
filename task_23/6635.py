from itertools import *

def f(com):
    pos = 33
    for i in com:
        if i == "1": pos -= 3
        else: pos *= (-3)
    return pos

ans = []

for i in product(["1", "2"], repeat=13):
    ans.append(f(i))

print(set(i for i in ans if i < 0))
print(len(set(i for i in ans if i < 0)))