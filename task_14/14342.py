for p in range(int("o", 36)+1, 37):
    f = int("bo", p) + int("om", p) + int("bl4", p) - int("cng", p)
    if f == 0: print(p)
print(sorted("bolcgn"))