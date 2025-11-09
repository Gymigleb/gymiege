m = 1000000
nm = 100000000
for n in range(1,10000):
    nb = bin(n)[2:]
    if nb.count("1") % 2 == 0:
        nb += "0"
        nb = "10" + nb[2:]
    else:
        nb += "1"
        nb = "11" + nb[2:]
    ni = int(nb, 2)
    if ni > 40:
        if m >= ni:
            nm = min(nm, n)
            m = min(m, ni)
        print(n , ni)
print(nm, m)