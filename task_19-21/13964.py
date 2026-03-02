from functools import lru_cache
from sys import setrecursionlimit

def M(a, b):
    return (a-2, b), (a, b-2), (a//2 if a%2==0 else a//2 + 1, b), (a, b//2 if b%2==0 else b//2+1)

@lru_cache(None)
def f(a, b, deep):
    if deep <= 0: return "l", -1
    if a + b <= 108: return "l", 0
    if all(f(*m, deep - 1)[0] == "w" for m in M(a, b)): return "l", max(f(*m, deep - 1)[1] for m in M(a, b)) + 1
    return "w", min(f(*m, deep - 1)[1] for m in M(a, b) if f(*m, deep - 1)[0] == "l") + 1

print(48*2*2)
print("20)", sorted([s for s in range(49, 200) if f(60, s, 5) == ("w", 3)]))
print("21)", sorted([s for s in range(49, 200) if f(60, s, 5) == ("l", 4)]))