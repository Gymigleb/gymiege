with open("9832.txt") as f:
    data = [list(map(int, i.split())) for i in f]

for i in data:
    u1 = [i.count(j) for j in i]
    if u1.count(2) == 4 and u1.count(1) == 3:
        if i.count(max(i)) == 1:
            print(sum(i))
            break