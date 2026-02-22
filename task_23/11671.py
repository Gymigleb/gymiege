from itertools import *

def f(s):
    pos = 1
    for i in s:
        if i == "a": pos += 10
        else: pos -=5
    return pos

ans = set()

for i in product("ab", repeat=15):
    i = "".join(i)
    ans |= set([f(i)])

print(ans)
print(len(ans))