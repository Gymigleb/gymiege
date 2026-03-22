from functools import lru_cache

def M(a, b):
    return (a+5, b), (a, b+5), (a*2, b), (a, b*2)

@lru_cache(None)
def f(a, b, deep):
    if deep == 0: return "l", -1
    if a * b > 384: return "l", 0
    if all(f(m[0], m[1], deep - 1)[0] == "w" for m in M(a, b)): return "l", max(f(m[0], m[1], deep - 1)[1] for m in M(a, b)) + 1
    return "w", min(f(m[0], m[1], deep - 1)[1] for m in M(a, b) if f(m[0], m[1], deep - 1)[0] == "l") + 1

# for i in range(400, 1, -1): f(8, i, 100)
print("19)", min(s for s in range(1, 55) if any(f(m[0], m[1], 100) == ("w", 1) for m in M(8, s))))
# print(*[(s, f(8, s, 1000)) for s in range(1, 55)], sep="\n")
print("20)", min(s for s in range(1, 55) if f(8, s, 100) == ("w", 3)), max(s for s in range(1, 55) if f(8, s, 100) == ("w", 3)))
print("21)", list(s for s in range(1, 55) if f(8, s, 100) == ("l", 4)))
for s in [6]:
    print(*[(s, m, f(m[0], m[1], 100)) for m in M(8, s)], sep="\n")