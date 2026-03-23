with open("17550.txt") as f:
    data = [list(map(int, i.split())) for i in f]

cnt = 0

for i in data:
    amount = [i.count(j) for j in i]
    if amount.count(3) == 3 and amount.count(1) == 3:
        pov = sum([j for j in i if i.count(j) > 1])**2
        nepov = sum([j for j in i if i.count(j) == 1])**2
        if pov > nepov: cnt += 1

print(cnt)