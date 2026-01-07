def f (n):
    out = ""
    while n:
        out += str(n % 4)
        n //= 4
    return out[::-1]
Mz = 0
Mx = 1000000000
for x in range(1, 3001):
    a = 4**210 + 4**110 - x
    at = f(a)
    if at.count("0") > Mz:
        Mx = x
        Mz = at.count("0")

print(Mx)
