m = 100000

for n in range(1, 10000):
    nb = bin(n)[2:]
    if n % 8 == 0:
        nb += nb[-2:]
    else:
        nb += bin(n % 8 * 2)[2:]
    
    r = int(nb, 2)
    if r > 3000:
        m = min(n, m)

print(m)