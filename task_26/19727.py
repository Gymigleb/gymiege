with open("./files/26.2_19727.txt") as f:
    m, n = map(int, f.readline().split())
    boxes = [int(i) for i in f]

boxes.sort()

cnt = 0

for box in boxes:
    if box <= m:
        m -= box
        cnt += 1
        last = box
    else: break

print(cnt, len([i for i in boxes if i > m + last]))