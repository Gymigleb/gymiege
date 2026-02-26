from itertools import *

def f(s):
    pos = 1
    for i in s:
        if i == "a": pos += 1
        elif i == "b": pos += 5
        else: pos *= 3
    return pos

ans = set()

for i in product("abc", repeat=8):
    i = "".join(i)
    a = f(i)
    if 1000 <= a <= 1024:
        ans |= {a}

print(ans)
print(len(ans))