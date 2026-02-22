def f(st, en, ex):
    if st == en: return 1
    if st < en or st == ex: return 0
    return f(st-1, en, ex) + f(st//2, en, ex)

print(f(30, 8, -1) * f(8, 1, -1))