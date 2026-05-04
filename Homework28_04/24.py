with open("./files/1_24.txt") as f:
    start = f.readline().strip()

s = start.replace("BC", "B C").split()
# print("BC".join(s[:2]))
ans = []
for i in range(len(s) - 190):
    targ = "".join(s[i:i+191])
    ans.append([len(targ), targ, targ.count("BC")])

print(max(ans), max(ans)[0])