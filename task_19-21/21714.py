from functools import lru_cache

def M(s):
    return s + 2, s + 5, s * 2

@lru_cache(None)
def f(s):
    if s >= 128: return "l", 0
    if all(f(m)[0] == "w" for m in M(s)): return "l", max(f(m)[1] for m in M(s)) + 1
    return "w", min(f(m)[1] for m in M(s) if f(m)[0] == "l") + 1


print("19)", [s for s in range(127, 0, -1) if f(s) == ("l", 2)])
print("20)", [s for s in range(127, 0, -1) if f(s) == ("w", 3)])
print("21)", [s for s in range(127, 0, -1) if f(s) == ("l", 4) and any(f(m) == ("w", 1) for m in M(s))])