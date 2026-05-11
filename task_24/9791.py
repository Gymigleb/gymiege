from re import *
from string import printable

with open("./files/24_9791.txt") as f:
    s = f.readline().strip()

pat = f"[{printable[1:16].upper()}][{printable[:16].upper()}]*"

ans = [m.group() for m in finditer(pat, s)]
print(len(max(ans, key=len)))


with open("./files/24_9791.txt") as f:
    s = f.readline().strip().lower()

for i in printable[16:]: s = s.replace(i, " ")
s = s.split()

print(len(max(ans, key=len)))


with open("./files/24_9791.txt") as f:
    s = f.readline().strip().lower()

cnt = 0
M = 0
for i in range(len(s)):
    if s[i] in printable[:16]:
        cnt += 1
    else:
        M = max(M, cnt)
        cnt = 0

print(max(M, cnt))