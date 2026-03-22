def f(n):
    out = ""
    while n:
        out += str(n%5)
        n //= 5
    return out[::-1]

ans = []

for n in range(1, 10000):
    n = 41
    r = f(n)
    if sum(map(int, list(r))) % 5 == 0:
        r = r.replace("1", "*")
        r = r.replace("0", "1")
        r = r.replace("*", "0")
        r += "14"
    else:
        r += "33"
        r = "44" + r[2:]
    r = int(r, 5)
    if r > 370:
        ans.append((r, n))
print(sorted(ans, reverse=True)[-1])
print(41)