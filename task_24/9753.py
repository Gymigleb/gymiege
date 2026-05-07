with open("./files/24_9753.txt") as f:
    s = f.readline().strip()

s = s.split("Y")

ans = []
k = 150

for i in range(len(s) - k):
    t = "Y".join(s[i : i+k+1])
    ans.append([len(t), t, t.count("Y")])

print(max(ans))


with open("./files/24_9753.txt") as f:
    s = f.readline().strip()
#    l
#     r
# s = "Y*******Y*****Y**************"

l = 0
r = 0
cnt = 0
ans = []
k = 150
# k = 2

while r < len(s)-1:
    if cnt <= k:
        if s[r] == "Y": cnt += 1
        r += 1
    else:
        ans.append([r-1 - l, s[l:r-1], s[l:r-1].count("Y")])
        while s[l] != "Y": l += 1
        l += 1
        cnt -= 1

ans.append([r - l, s[l:r], s[l:r].count("Y")])
print(max(ans))