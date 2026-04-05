def f(st, en, ex):
    if st == ex or st < en: return 0
    if st == en: return 1
    return f(st-1, en, ex) + f(st-4, en, ex) + f(st//3, en, ex)

print(f(19, 13,7)* f(13, 2,7))