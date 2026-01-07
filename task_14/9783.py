from string import printable
for x in printable[:22]:
    a = int(f"18{x}89957", 22)
    b = int(f"80{x}33", 22)
    c = int(f"521{x}6", 22)
    if (a + b + c) % 21 == 0:
        print((a + b + c) // 21)
