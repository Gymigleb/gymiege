from itertools import *

with open("./files/24_7600.txt") as f:
    s = f.readline().strip()

ex = list(product("QRS", "QRS"))

for i in ex:
    i = "".join(i)
    s = s.replace(i, f"{i[0]} {i[1]}")

s = s.split()

print(len(max(s, key=len)))