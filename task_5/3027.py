def s(a):
    su = 0
    for i in range(len(a)):
        su += int(a[i])
    return su

count = 0

for n in range(1000):
    nb = bin(n)[2:]
    if n % 2 == 0:
        nb += bin(s(nb))[2:]
    else:
        nb = "1" + nb + "00"
    r = int(nb, 2)
    if r >= 500 and r <= 700:
        count += 1
        print(n , r)
print(count)