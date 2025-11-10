M = 0
for n in range(10000):
    nb = bin(n)[2:]
    if n % 3 == 0:
        nb += nb[-3:]
    else:
        nb += bin(n%3*3)[2:]
    r = int(nb, 2)
    if r <= 170:
        print(n, r)
        M = max(M, r)
print(M)