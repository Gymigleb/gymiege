def f(n):
    out = []
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            out += [d, n // d]
    return out

cnt = 0

for i in range(10**9, 10**100):
    s = str(i)
    if s == s[::-1]:
        d = f(i)
        m = max(d)
        if m % 7 == 0:
            print(i, m)
            cnt += 1
            if cnt >= 5: break