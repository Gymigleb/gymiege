for n in range(1,100000000):
    nb = bin(n)[2:]
    if sum(map(int, nb)) % 2 == 0:
        nb  = "11" + nb[2:] + "1"
    elif nb.count("0") < nb.count("1"):
        nb += "0"
    else: nb += "1"

    r = int(nb, 2)

    if r > 271:
        print(n, r)
        break