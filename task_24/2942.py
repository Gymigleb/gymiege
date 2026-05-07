with open("./files/24_2942.txt") as f:
    s = f.readline().strip()

# s = "AACCBABCACACABBBBBACACACACACABAB"
s = " " + s + " "

for i in range(2):
    s = s.replace("AA", "A A")
    s = s.replace("BB", "B B")
    s = s.replace("CC", "C C")
    s = s.replace("BC", "B C")
    s = s.replace("CB", "C B")
    s = s.replace(" C", " C ")
    s = s.replace(" B", " B ")
    s = s.replace("A ", " A ")

s = s.split()

# print(s)

print(len(max(s, key=len))/2)

with open("./files/24_2942.txt") as f:
    s = f.readline().strip()

# s = "AACCBABCACACABBBBBACACACACACABAB"

l = 0
r = 0
ans = []
while r < len(s):
    # print(" "*l + s[l:r+1], s[r:r + 2], l, r)
    if s[r:r+2] in ["AB", "AC"]:
        r += 2
    else:
        ans.append(s[l:r])
        l = r+1
        r = l
ans.append(s[l:r])
print(len(max(ans, key=len))/2)


from re import *
with open("./files/24_2942.txt") as f:
    s = f.readline().strip()

pat = r"(A[BC])+"

m = finditer(pat, s)
arr = [i.group() for i in m]

print(len(max(arr, key=len))/2)


with open("./files/24_2942.txt") as f:
    s = f.readline().strip()

i = 0
cnt = 0
ans = 0
while i < len(s) - 1:
    if s[i: i+2] in "AB AC":
        cnt += 1
        i += 2
    else:
        ans = max(ans, cnt)
        cnt = 0
        i += 1

ans = max(ans, cnt)
print(ans)