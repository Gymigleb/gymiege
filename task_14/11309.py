from string import printable

for x in printable[:27]:
    a = int(f"8{x}38{x}68", 27)
    b = int(f"37{x}3163", 27)

    if (a + b) % 26 == 0:
        print((a + b) // 26)