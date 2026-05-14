with open("./files/24_21717.txt") as f:
    s = f.readline().strip()

s = s.replace("RSQ", "Rsq rsQ")
s = s.split()
k = 130
ans = []

for i in range(len(s) - k + 1):
    t = "".join(s[i:i+k-1])
    t = t.replace("sqrs", "S").upper()
    for j in s[i + 129][3:]:
        if j in "Qq": t += "Q"
        else:
            break
    t += j
    ans.append([len(t), t, t.count("RSQ")])

print(min(ans))