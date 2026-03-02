from functools import lru_cache

def M(a, b):
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)

@lru_cache(None)
def f(a, b):
    if a + b >= 259: return "l", 0
    if all(f(*m)[0] == "w" for m in M(a, b)): return "l", max(f(*m)[1] for m in M(a, b)) + 1
    return "w", min(f(*m)[1] for m in M(a, b) if f(*m)[0] == "l") + 1

print((259 - 17)/2/2)
print("20)", sorted([s for s in range(241, 0, -1) if f(17, s) == ("w", 3)]))
print("20)", sorted([s for s in range(241, 0, -1) if f(17, s) == ("l", 4)]))
# for s in range(241, 0, -1):
#     print(s, f(17, s), s+17)