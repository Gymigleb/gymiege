from functools import lru_cache

def M(s):
    a, b = s
    out = [[a+4, b], [a, b+4], [a*3, b], [ a, b*3]]
    for i in range(4):
        out[i] = sorted(out[i])
    return out

@lru_cache(None)
def f(x, y):
    s = x, y
    if sum(s) >= 154: return "L", 0
    if all(f(*m)[0] == "W" for m in M(s)):
        return "L", max(f(*m)[1] for m in M(s)) + 1
    return "W", min(f(*m)[1] for m in M(s) if f(*m)[0] == "L") + 1

# print(*[[s, f(20, s)] for s in range(1, 143)], sep="\n")
print("19)", min(s for s in range(1, 143) if any(f(*m) == ("W", 1) for m in M([20, s]))))
print("20)", [s for s in range(1, 143) if f(20, s) == ("W", 3)])
print("20)", [s for s in range(1, 143) if f(20, s) == ("L", 4) and any(f(*m) == ("W", 1) for m in M([20, s]))])