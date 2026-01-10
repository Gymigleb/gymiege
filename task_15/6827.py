from itertools import *

l = [x + e for x in range(5, 1001) for e in (0, 0.1, 0.9)]
ans = []
l1 = [x + e for x in sorted([257, 5, 100, 1000, 99, 258]) for e in (0, 0.1, 0.9)]

def f(x):
    p = 257 <= x <= 1000
    q = 5 <= x <= 100
    r = 99 <= x <= 258
    a = s <= x <= e
    return (a <= r) and ((not (a <= p)) <= q)
    # return ((not a) or r) and ((not a) or p or q)

def progress():
    print("work complited: ", work_cnt/work_size, "%", sep="")


for s, e in combinations(l1, 2):
    if all(f(x) for x in l1):
        ans.append(e - s)
print(min(ans), "ans by l1")
ans = []


work_size = sum(1 for i in combinations(l, 2))
work_cnt = 1
print(work_size)
progress()
print(work_size)

for s, e in combinations(l, 2):
    if all(f(x) for x in l):
        ans.append(e - s)
    if work_cnt % 100000 == 0: progress()
    work_cnt += 1

print(min(ans))