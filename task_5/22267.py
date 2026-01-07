def f(n):
    out = ""
    while n:
        out += str(n%7)
        n //= 7
    return out[::-1]

M = 0
nm = 0

for n in range(1, 100000):
    r = f(n)
    if r[-1] == "2":
        r = r.replace("1", "*")
        r = r.replace("3", "1")
        r = r.replace("*", "3")
        r = "21" + r
    else:
        r = "1" + r[1:] + "36"
    r = int(r, 7)
    if r < 744:
        if r > M:
            M = r
            nm = n
print(nm)
