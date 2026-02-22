def f(st, en):
    if st == en: return 1
    if st > en: return 0
    if st == 6: return f(st+2, en) + f(st+5, en)
    return f(st+2, en) + f(st+5, en) + f(st**2, en)

print(f(4, 36))