with open("./files/24_20909.txt") as f:
    s = f.readline().strip()

s = s.replace("AB", "A B")
s = s.split()

k = 100
ans = []

for i in range(len(s)-k):
    t = "".join(s[i:i+k+1])
    ans.append([len(t), t, t.count("AB")])

print(max(ans))