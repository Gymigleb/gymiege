M = 0

for n in range(1, 1000000):
    nb = bin(n)[2:]
    if nb.count("0") % 2 == 0:
        nb = "1" + nb + "1"
    else:
        nb = "10" + nb

    r = int(nb, 2)
    if r < 100:
        M = max(M, r)

print(M)