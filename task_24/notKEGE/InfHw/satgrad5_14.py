from string import ascii_uppercase as alph

with open("./satgrad5_14.txt") as f:
    data = f.readline().strip()

# data = "01BA1C1EF499AB9"

def f(s, target):
    out = []
    for i in range(0, len(s)):
        if s[i] == target: out.append(i)
    arr = []
    for i in range(len(out)-1):
        arr.append(s[out[i]: out[i+1]+1])
    return arr

gl = "AEIOUY"
start = data
ans = []

for i in gl: start = start.replace(i, "A")
for i in alph:
    if i not in gl:
        start = start.replace(i, "B")

for i in "02468": start = start.replace(i, " ")

for target in "13579":
    s = start
    for i in "13579":
        if i != target:
            s = s.replace(i, " ")
    # print(s)
    s = s.split()
    for i in s:
        if i.count(target) >= 2:
            arr = f(i, target)
            for j in arr:
                if j.count("A") == j.count("B"):
                    ans.append(j)
ans = sorted(ans, key=len, reverse=True)
# print(ans)
# print(start.find(ans[0]))
maxlen = len(ans[0])
ansInd = []
for i in ans:
    if len(i) != maxlen: break
    ansInd.append(start.find(i))
print(max(ansInd))