# 2345
def f(s, e):
    if start == end: return 1
    if start < end: return 0
    return f(s-1 ,e) + f(s-3 ,e) + f(s//3 ,e)