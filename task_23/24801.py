def f(st, en, ex):
    if st == ex or st > en: return 0
    if st == en: return 1
    return f(st+1, en, ex) + f(st+2, en, ex) + f(st+4, en, ex) + f(st+8, en, ex)

a = f(16, 24, 32)* f(24, 48, 32)
b = f(16, 32, 24)* f(32, 48, 24)
print(a, b)
print(a+b)