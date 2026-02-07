from fnmatch import fnmatch

def f(n):
    out = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            out |= {d, n // d}
    return out

for i in range(0, 10**7+1, 53):
    s = str(i)
    if fnmatch(s, "*2?2*") and s == s[::-1]:
        d = f(i)
        if len(d) > 30:
            print(i, sum(d))
