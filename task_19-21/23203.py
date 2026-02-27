from functools import lru_cache

def M(s):
    return s - 3, s - 7, s // 3

@lru_cache(None)
def f(s):
    if s <= 11: return "l", 0
    if all(f(m)[0] == "w" for m in M(s)): return "l", max(f(m)[1] for m in M(s)) + 1
    return "w", min(f(m)[1] for m in M(s) if f(m)[0] == "l") + 1

def g(x, s):
    if x <= 11: return s % 2 == 0
    if s <= 0: return False 
    m = [g(x-3, s-1), g(x-7, s-1), g(x//3, s-1)]
    return any(m) if (s - 1) % 2 == 0 else all(m)

for s in range(12, 1000):
    if f(s) == ("l", 2):
        print(s, "ans on 19")
    # else: print(s, f(s))

for s in range(12, 1000):
    if f(s) == ("w", 3) and not f(s) == ("w", 1):
        print(s, "ans on 20")

for s in range(12, 1000):
    if f(s) == ("l", 4) and  any(f(m) == ("w", 1) for m in M(s)):
        print(s, "ans on 21", [(m, f(m)) for m in M(s)])

# П В
print("another code")
for x in range(12, 1000):
    if g(x, 2):
        print(x, "ans on 19", f(x), g(x, 2))
    # else: print(x, f(x))

for x in range(30, 117):
    if not g(x, 1) and g(x, 3): print(x, "ans on 20")
    # print(x, f(x), g(x, 1), g(x, 3))

for x in range(30, 117):
    if not g(x, 4) and not g(x, 2): print(x, "ans on 21")
    # print(x, f(x), g(x, 1), g(x, 3))

print("ans 19) 36; 20) 39 40; 21) 42")