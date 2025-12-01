alf = "02468ace"

rm = 100000000

for n in range(151, 1000000):
    nh = hex(n)[2:]
    nh = nh.replace("a", "1")
    s = 0
    for a in alf:
        s += nh.count(a)
    if s > 2: nh += "b"
    else: nh = "f" + nh
    r = int(nh, 16)
    if r > 3500:
        rm = min(rm, r)

for n in range(151, 1000000):
    nh = hex(n)[2:]
    nh = nh.replace("a", "1")
    s = 0
    for a in alf:
        s += nh.count(a)
    if s > 2: nh += "b"
    else: nh = "f" + nh
    r = int(nh, 16)
    if r == rm:
        print(n, r)