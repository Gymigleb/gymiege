for n in range(100):
    nb = bin(n)[2:]
    if n % 5 == 0:
        nb = nb + nb[-3:]
    else:
        nb += bin(n%5*5)[2:]

    r = int(nb, 2)
    if r > 256: print(n, r)