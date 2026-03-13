from functools import lru_cache

def M(s):
    return s-2, s//1.5

@lru_cache(None)
def f(s, deep):
    if s < 14: return "l", 0
    if deep == 0: return "l", -1
    if all(f(m, deep - 1)[0] == "w" for m in M(s)): return "l", max(f(m, deep - 1)[1] for m in M(s)) + 1
    return "w", min(f(m, deep - 1)[1] for m in M(s) if f(m, deep - 1)[0] == "l") + 1

print("19)", min(s for s in range(14, 100) if f(s, 100) == ("l", 2)))
print("20)", sorted(s for s in range(14, 100) if f(s, 100) == ("w", 3)))
print("21)", min(s for s in range(14, 100) if f(s, 100) == ("l", 4) and any(f(m, 100) == ("w", 1) for m in M(s))))
