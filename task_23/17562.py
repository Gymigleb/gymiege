def f(st, en):
    if st == en: return 1
    if st > en: return 0
    return f(st+1, en) + f(st+2, en) + f(st+3, en)

print(f(5, 7) * f(7, 11))