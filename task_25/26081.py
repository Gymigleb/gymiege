out = []

for i in range(1, 13):
    for j in range(113, 113001, 113*2):
        n = 3**i + j
        if 100000 <= n < 1000000 and str(n).count("0") == 0:
            out.append((n, i))

out.sort()

for i in out[:5]:
    print(*i)
