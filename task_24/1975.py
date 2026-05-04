with open("./files/24_1975.txt") as f:
    s = f.readline().strip()

s = s.replace("PP", "P P")
s = s.replace("PP", "P P")
s = s.split()

print(len(max(s, key=len)))

with open("./files/24_1975.txt") as f:
    s = f.readline().strip()

# s = "aPPaaaaa"

l = 0
r = 0
ans = []
while r <= len(s):
    # print(" "*l + s[l:r+1], s[r:r + 2], l, r)
    if s[r:r + 2] != "PP":
       r += 1
    else:
        ans.append(s[l:r+1])
        l = r+1
        r = l

ans.append(s[l:r+1])
print(len(max(ans, key=len)))

from re import *
with open("./files/24_1975.txt") as f:
    s = f.readline().strip()

# s = "aPPaaaaa"

pat = r"[^P]*(P[^P]+)*P?"

m = finditer(pat, s)
arr = [i.group() for i in m]

print(len(max(arr, key=len)))