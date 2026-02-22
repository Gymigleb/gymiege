def f(st, ed, ex):
    if st == ed: return 1
    if st < ed or st == ex: return 0
    return f(st-2, ed, ex) + f(st//2, ed, ex)

print(f(32, 14, -1) * f(14, 1, -1))