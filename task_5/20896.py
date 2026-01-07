for n in range(1, 10000000):
    nb = bin(n)[2:]
    if nb.count("1") % 2 == 0:
        nb = "10" + nb[2:] + "0"
    else:
        nb = "11" + nb[2:] + "1"
    r = int(nb, 2)
    if r > 19:
        print(n, r)
        break