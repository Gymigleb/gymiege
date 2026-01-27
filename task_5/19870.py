def f(n):
    out = ""
    while n:
        out += str(n%4)
        n //= 4
    return out[::-1] if out else "0"

m = 10**10

for n in range(0, 10000):
    r = f(n)
    if n%2 == 0:
        r = "12" + r + f(int(r[-1])*3)
    else:
        r = "21" + r + "13"

    r = int(r, 4)

    if r > 50:
        m = min(r, m)

print(m)