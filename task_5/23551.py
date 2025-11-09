m = 0
nm = 0
for n in range(1,10000):
    nb = bin(n)[2:]
    if n % 2 == 0:
        nb = "10" + nb
    else:
        nb = "1" + nb + "01"
    ni = int(nb, 2)
    if ni < 30:
        if m <= ni:
            nm = max(nm, n)
            m = max(m, ni)
        print(n , ni)
print(nm, m)