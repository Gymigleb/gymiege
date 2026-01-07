from string import printable
for x in printable[:19]:
    a = int(f"98{x}79641", 19)
    b = int(f"36{x}14", 19)
    c = int(f"73{x}4", 19)
    if (a + b + c) % 18 == 0:
        print((a + b + c) // 18)
