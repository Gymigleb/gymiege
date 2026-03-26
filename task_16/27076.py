from functools import lru_cache
from types import NoneType

@lru_cache(None)
def f(n):
    if n < 43: return g(n+4)
    return 2*f(n-2)-f(n-4)+2

@lru_cache(None)
def g(n):
    if n < 11240:
        return g(n+3)+2
    return q(n)

@lru_cache(None)
def q(n):
    if n < 21:
        return n + 4
    return q(n-4) + 2

for i in range(20, 10000): q(i)
for i in range(12000, 42, -1): g(i)


print(f(2026))