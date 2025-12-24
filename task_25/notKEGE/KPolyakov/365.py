def f(n):
    out = []
    d = 2
    while d**2 <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1: out.append(n)
    return sorted(out)

# print(f(10))
# print(f(11))
# print(f(25))

cnt = 0

for i in range(6_651_221, 10**10):
    d = f(i)
    if len(d) == 2 and str(d[0]).count("2") == 1 and str(d[1]).count("2") == 1:
        print(cnt, i, d)
        cnt += 1
    if cnt >= 5: break