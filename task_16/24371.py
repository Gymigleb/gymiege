from functools import lru_cache

@lru_cache(None)
def g(n):
    if n < 100: return n
    return f(n-3) + 1

def f(n):
    return g(n-2)

for i in range(5001): g(i)

print(f(5000))