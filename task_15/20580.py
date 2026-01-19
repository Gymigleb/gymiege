from itertools import *

def f(a):
    return all((9*x + y > a) or (x >= 36) or (y >= 18) for x in range(1, 10000) for y in range(1, 10000))

for a in range(1, 1000000):
    if f(a): print(a)