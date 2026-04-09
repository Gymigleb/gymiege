with open("./6_24.txt") as f:
    s = f.readline().strip()

a = "2025"
cntA = 50
cntY = 140
# a = "-="
# s = "-=YY-=YY-=yyyyyyyyyyyy"
# cntA = 2
# cntY = 3

s = s.replace(a, a+" ")
s = s.split()
# print(s)
last = ""
cnt_max = 0

for _ in range(len(s)-cntA):
    i = "".join(s[_:_+cntA+1])
    # print(i)
    if i[-len(a):] == a:
        for j in range(0, len(i)):
            # print(i[j:])
            if i[j:].count("Y") >= cntY and i[j:].count(a) == cntA:
                if cnt_max < len(i[j:]):
                    last = i[j:]
                cnt_max = max(cnt_max, len(i[j:]))
                # print("#######", i[j:], len(i[j:]))
            if i[j:].count("Y") < cntY or i[j:].count(a) < cntA: break

print(cnt_max, last, last.count("Y"), last.count(a))