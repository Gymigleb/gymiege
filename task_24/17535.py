with open("./files/24_17535.txt") as f:
    s = f.readline().strip()

s = s.replace("CD", "C D")
s = s.split()
k = 160

ans = []

for i in range(len(s) - k + 1):
    t = "".join(s[i:i+k+1])
    ans.append([len(t), t, t.count("CD")])

print(max(ans))