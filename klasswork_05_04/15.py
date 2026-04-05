def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = st <= x <= en
    return p <= ((q and (not a)) <= (not p))

lineA = [15, 21, 40, 63]
lineB = [14, 16, 22, 41, 65]

for st in lineA:
    for en in lineA:
        if all(f(x) for x in lineB):
            print(en-st)