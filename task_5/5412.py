from itertools import count

count = 0

for n in range(1, 1000000):
    nh = hex(n)[2:]
    if nh.count("b") % 2 == 0:
        nh = "1" + nh
    else:
        nh += "1"
    r = int(nh, 16)
    if len(str(r)) == 2:
        count += 1

print(count)