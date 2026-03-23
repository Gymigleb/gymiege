with open("9740.txt") as f:
    data = [list(map(int, i.split())) for i in f]

ans = 0

for i in data:
    cnt = [i.count(j) for j in i]
    if cnt.count(1) == 4:
        pov = [j for j in i if i.count(j) > 1][0]
        nepov = sum([j for j in i if i.count(j) == 1])/4
        if pov >= nepov:
            ans += 1

print(ans)