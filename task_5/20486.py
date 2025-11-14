m = 10000000
for n in range(3,10000):
    nb = bin(n)[2:]
    if n % 2 == 0:
        nb = nb+nb[:3]
    else:
        nb = "1" + nb + "01"
    
    r = int(nb, 2)

    if r > 600:
        print(n, r)
        m = min(r,m)
print(m)