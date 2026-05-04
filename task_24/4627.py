with open("./files/24_4627.txt") as f:
    s = f.readline().strip()

s = s.replace("NPO", "+").replace("PNO", "+")
s = s.replace("N", " ").replace("P", " ").replace("O", " ")
s = s.split()

print(len(max(s, key=len)))


with open("./files/24_4627.txt") as f:
    s = f.readline().strip()
 
ans = 0

for i in range(len(s) - 2):
    if s[i:i + 3] in "PNO NPO":
        cnt = 1
        for j in range(i + 3, len(s) - 2, 3):
            if s[j:j + 3] in "PNO NPO": cnt += 1
            else: break
        ans = max(ans, cnt)

print(ans)


from re import *
with open("./files/24_4627.txt") as f:
    s = f.readline().strip()

p = r"((PN|NP)O)+"
p = r"(PNO|NPO)+"
m = finditer(p, s)
arr = [i.group() for i in m]

print(len(max(arr, key=len))//3)