with open("./files/26_16390.txt") as f:
    s, n = map(int, f.readline().split())
    boxes = [int(i) for i in f]

boxes.sort()

cnt = 0

for box in boxes:
    if box <= s:
        s -= box
        cnt += 1
        last = box
    else: break

print(cnt, max(i for i in boxes if s+last >= i))