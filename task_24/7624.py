from itertools import *

with open("./files/24_7624.txt") as f:
    s = f.readline().strip()

ex = list(product("XYZ", "XYZ"))

for i in range(len(ex)): ex[i] = "".join(ex[i])

M = 0
cnt = 0
for i in range(len(s)-1):
    if s[i:i+2] not in ex:
        cnt += 1
    else:
        cnt += 1
        M = max(M, cnt)
        cnt = 0

print(M)