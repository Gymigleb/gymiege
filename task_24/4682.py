with open("./files/24_4682.txt") as f:
    s = f.readline().strip()

alA = "AE"
alB = "BCD"

for i in alA: s = s.replace(i, "A")
for i in alB: s = s.replace(i, "B")

cnt = 0
while "AB" * cnt in s:
    cnt += 1

print(cnt - 1)