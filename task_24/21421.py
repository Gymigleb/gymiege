from re import *

with open("./files/24_21421.txt") as f:
    s = f.readline().strip()

pat = r"[1-9AB][0-9AB]*[02468A]"

ans = [m.group() for m in finditer(pat, s)]

print(len(max(ans, key=len)))


from string import printable

with open("./files/24_21421.txt") as f:
    s = f.readline().strip().lower()

s = " " + s + " "
for i in printable[1:12:2]: s = s.replace(i, "1")
for i in printable[2:12:2]: s = s.replace(i, "2")
for i in printable[12:]: s = s.replace(i, " ")

while " 0" in s: s = s.replace(" 0", " ")
while "1 " in s: s = s.replace("1 ", " ")

s = s.split()

print(len(max(ans, key=len)))


with open("./files/24_21421.txt") as f:
    s = f.readline().strip().lower()

for i in printable[12:]: s = s.replace(i, " ")

s = s.split()

ans =  [i.lstrip("0").rstrip("13579b") for i in s]
print(len(max(ans, key=len)))


with open("./files/24_21421.txt") as f:
    s = f.readline().strip().lower()

l = r = 0
ans = []
start = False
while r < len(s):
    if s[r] not in printable[12:] and start:
        if s[r] in "2468A":
            ans.append(s[l: r+1])
    elif s[r] not in printable[12:] and s[r] != "0":
        start = True
        if s[r] in "2468A":
            ans.append(s[l: r+1])
    else:
        l = r + 1
        start = False
    r += 1

print(len(max(ans, key=len)))