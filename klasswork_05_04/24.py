with open("./24.txt") as f:
    s = f.readline().strip()

k = 270
# k = 3
# s = "AAAZAAAAAZBZDZ"
M = 10**100

print(s[:10],"..." , s[-10:], sep="")

s = s.split("Z")
print(s[:5])

for i in range(len(s)-k+1):
    cur = s[i:i + k - 1]
    if i == 0 or i == len(s)-k:
        if i == 0: cur = "Z".join(cur)+"Z"
        else: cur = "Z"+"Z".join(cur)+"Z"
        # print(cur,"if")
        if cur.count("Z") == k:
            M = min(M, len((cur)))
    else:
        cur = "Z"+"Z".join(cur)+"Z"
        if cur.count("Z") == k:
            M = min(M, len((cur)))
        # print(cur, "else")

print(M)