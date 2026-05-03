with open("./files/1_24.txt") as f:
    start = f.readline().strip()

s = start.split("BC")
# print("BC".join(s[:2]))
ans = []
for i in range(len(s) - 190):
    targ = "BC".join(s[i:i+191])
    ans.append([targ, targ.count("BC"), len(targ)])

print(max(ans))