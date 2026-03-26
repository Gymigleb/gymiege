with open("./files/14251.txt") as f:
    data = [list(map(int, i.split())) for i in f]

for i in data:
    amount = [i.count(j) for j in i]
    if amount.count(2) == 4 and amount.count(1) == 3:
        pov = sum(j for j in i if i.count(j) > 1)
        nech = sum(j for j in i if j % 2 != 0)
        if pov <= nech:
            print(sum(i))
            break