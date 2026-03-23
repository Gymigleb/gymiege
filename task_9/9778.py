with open("9778.txt") as f:
    data = [list(map(int, i.split())) for i in f]

for num, i in enumerate(data, start=1):
    cnt = [i.count(j) for j in i]
    if cnt.count(1) == 4:
        pov = [i[j] for j in range(6) if cnt[j] > 1][0]
        nepov = sum([i[j] for j in range(6) if cnt[j] == 1])/4
        if pov >= nepov:
            print(num)
            break