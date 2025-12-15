f = open("24_25361.txt")

s = f.readline()

for i in "02468":
    s = s.replace(i, " 0")

s = s.split()
s = s[1:]

M = 0

def f(s):
    cnt = 0
    for i in range(0, len(s)):
        if s[i] == "F": cnt += 1
        if cnt == 77: return i

for i in s:
    if i.count("F") >= 76:
        M = max(M, f(i))

print(M)