def f(n):
    out = []
    cnt = 0
    for d in range(int(n**0.5) - 120, int(n**0.5) + 1):
        if n % d == 0:
            if abs(n // d - d) <= 120:
                cnt += 1
                out.append(d)
                out.append(n // d)
    if len(out) == 0: return cnt, 0
    return cnt, max(out)

for i in range(2*10**6, 3*10**6):
    ans = f(i)
    if ans[0] >= 3:
        print(i, ans[1])
