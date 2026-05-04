from re import *

with open("./files/24_4602.txt") as f:
    s = f.readline().strip()

p = r"([BCD][AO])*"
m = finditer(p, s)
arr = [i.group() for i in m]

print(len(max(arr, key=len))//2)


with open("./files/24_4627.txt") as f:
    s = f.readline().strip()
 
ans = 0

for i in range(len(s) - 1):
    if s[i] in "BCD" and s[i+1] in "AO":
        cnt = 1
        for j in range(i + 2, len(s) - 1, 2):
            if s[j] in "BCD" and s[j+1] in "AO": cnt += 1
            else: break
        ans = max(ans, cnt)

print(ans)
