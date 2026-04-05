def f(n):
    out = ""
    while n:
        out += str(n%4)
        n //= 4
    return out[::-1] if len(out) != 0 else "0"

m = 10**100

for n in range(1, 100000):
    r = f(n)
    if n % 4 == 0:
        r += r[:2]
    else:
        r += f(n%4*4)
    r = int(r, 4)
    if r > 291:
        m = min(m, r)

print(m)