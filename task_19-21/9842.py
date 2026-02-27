from functools import lru_cache

def M(s):
    return s + 1, s + 3, s * 4

@lru_cache(None)
def f(s):
    if s >= 111: return "l", 0
    if all(f(m)[0] == "w" for m in M(s)): return "l", max(f(m)[1] for m in M(s)) + 1
    return "w", min(f(m)[1] for m in M(s) if f(m)[0] == "l") + 1

for s in range(110, 0, -1):
    if f(s) == ("l", 2): print("19)", s)
    if f(s) == ("w", 3) and f(s) != ("w", 1): print("20)", s)
    if f(s) == ("l", 4) and any(f(m) == ("w", 1) for m in M(s)): print("21)", s)