with open("./files/26_12113.txt") as f:
    N = f.readline()
    boxes = [int(i) for i in f]

boxes.sort(reverse=True)

red_traser = [max(i for i in boxes if i%2 == 1)]
blue_traser = [max(i for i in boxes if i%2 == 0)]

for box in boxes:
    if red_traser[-1] % 2 != box % 2 and red_traser[-1] - box >= 7:
        red_traser.append(box)
    if blue_traser[-1] % 2 != box % 2 and blue_traser[-1] - box >= 7:
        blue_traser.append(box)

print(len(red_traser), red_traser[-1])
print(len(blue_traser), blue_traser[-1])