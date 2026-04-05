from functools import lru_cache

def M(s):
    return s-3, s-8, s//3

@lru_cache(None)
def f(s):
    if s <= 15: return "l", 0
    if all(f(m)[0] == "w" for m in M(s)): return "l", max(f(m)[1] for m in M(s))+1
    return "w", min(f(m)[1] for m in M(s) if f(m)[0] == "l") + 1

print("19)", min(s for s in range(16, 1000) if f(s) == ("l", 2)))
print("20)", sorted(s for s in range(16, 1000) if f(s) == ("w", 3)))
print("21)", min(s for s in range(16, 1000) if f(s) == ("l", 4)\
                 and any(f(m) == ("w", 1) for m in M(s))))