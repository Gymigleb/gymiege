f = open("24_10724.txt")

data = f.readline().strip().lower()

from string import printable

#regular#regular#regular#regular#regular#
from re import *
s = data
# print(s[:10])

pattern = r"[^g-z]*"
res = sub(pattern, "*", s)

# print(res[:10])
matches = finditer(pattern, data)
ans = set([m.group() for m in matches])
# print(ans)
# ans = ""
# cnt = 0
# for i in range(len(res)):
#     if res[i] == "*": ans += s[i]
#     else: s += " "
#     cnt += 1
#     if cnt%10000 == 0: print(cnt)
# print("out")
# ans = ans.split()
ans = [len(i.lstrip("0")) for i in ans]
# 72623
print(max(ans))

# exit(0)
#regular#regular#regular#regular#regular#

#type1#type1#type1#type1#type1#type1#
s = " " + data

for i in printable[16:]:
    s = s.replace(i, " ")

while " 0" in s: s = s.replace(" 0", " ")

s = s.split()

a = [len(i) for i in s]

print(max(a))
#type1#type1#type1#type1#type1#type1#