# with open("./2_26.txt") as f:
#     k = int(f.readline())
#     n = int(f.readline())
#     data = [list(map(int, i.split())) for i in f]
# # with open("./small.txt") as f:
# #     k = int(f.readline())
# #     n = int(f.readline())
# #     data = [list(map(int, i.split())) for i in f]

# hran =[]

# for num, (st, en) in enumerate(data):
#     hran.append((st, 0, num))
#     hran.append((en, 1, num))

# # print(hran)
# hran.sort()
# # print(hran)

# box = [(0, -1) for i in range(k)]
# cnt = 0

# for i in hran:
#     # print(box)
#     if i[1] == 0: 
#         for j in range(k):
#             f1 = False
#             if box[j][0] == 0:
#                 box[j] = (1, i[2])
#                 cnt += 1
#                 last = j
#                 f1 = True
#                 break
#         if not f1: print(i)
#     else:        
#         for j in range(k):
#             if box[j][1] == i[2]:
#                 box[j] = (0, -1)
#                 break
    
# print("gleb)", cnt, last+1)


with open("./2_26.txt") as f:
    k = int(f.readline())
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]
# with open("./small.txt") as f:
#     k = int(f.readline())
#     n = int(f.readline())
#     data = [list(map(int, i.split())) for i in f]

data.sort()

cels = [-1 for i in range(k)]
cnt = 0

for st, en in data:
    # print()
    # print(cels)
    for j in range(len(cels)):
        f1 = False
        if cels[j] < st:
            cels[j] = en
            cnt += 1
            last = j
            # print(st, en, j)
            f1 = True
            break
    if not f1: print(st, en)
    
print("another)", cnt, j+1)