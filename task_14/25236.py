for p in range(11, 37):
    a = int("29a1", p)
    b = int("47771", p)
    c = int("12a", p)
    if any(a+b+c == 1000000 + x for x in range(1, 500000+1)):
        print(p)