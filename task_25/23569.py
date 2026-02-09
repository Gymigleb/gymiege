def f(n):
    out = []
    for d in range(2, 3):
        while n % d == 0:
            out += [d]
            n //= d
            if len(out) > 2: return out

    for d in range(3, int(n**0.5) + 1, 2):
        while n % d == 0:
            out += [d]
            n //= d
            if len(out) > 2: return out
    return out + [n] if n > 1 else out

cnt = 0

for i in range(6_086_056, 10**100):
    d = f(i)
    if len(d) == 2:
        if str(d[0]).count("6") == 1 and str(d[1]).count("6"):
            print(i, max(d))
            cnt += 1
            if cnt >= 5: break