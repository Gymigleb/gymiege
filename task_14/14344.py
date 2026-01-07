from string import printable

for p in range(16, 36):
    a = int(f"17496", p)
    b = int(f"91f83", p)
    c = int(f"d9543", p)
    s = a + b + c

    if s % 12 == 0:
        print(p, s // 12)