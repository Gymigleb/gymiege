from string import printable

for x in printable[:13]:
    a = int(f"9{x}ab", 13)
    b = int(f"{x}46c", 16)
    c = int(f"b7{x}", 15)
    s = a + b - c

    if s % 14 == 0:
        print(x, s // 14)