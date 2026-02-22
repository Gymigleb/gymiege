def f(st, en, ex):
    if st == en: return 1
    if st > en or st == ex: return 0
    return f(st+1, en, ex) + f(st+2, en, ex) + f(st*3, en, ex)

print(f(2, 9, 16) * f(9, 18, 16))