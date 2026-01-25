f = open("24_18619.txt")

data = f.readline().strip()
s = data
s = s.replace("B", " B")
s = s.replace("A", " ")
s = s.replace("C", " ")
s = s.replace("D", " ")
s = " " + s + " "
s = s.replace("-", "*")
for i in range(2):
    while "**" in s: s = s.replace("**", "* *")
    while " *" in s: s = s.replace(" *", " ")
    while "* " in s: s = s.replace("* ", " ")

s = s.split()
M = 0
for i in s:
    if i[0] == "B" and len(i) > 1 and i[1] != "*":
        M = max(len(i), M)

print(M)

from re import *
s = data
s = s.replace("-", "*")
pattern = r"[B][^*ABCD][^ABCD]*[^*ABCD]"
matches = finditer(pattern, s)
ans = [m.group() for m in matches if "**" not in m.group()]
print(max(ans, key=len))
print(len(max(ans, key=len)))