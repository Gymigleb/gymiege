with open("./files/17_18176.txt") as f:
    data = [int(i) for i in f]
    m4 = min(i for i in data if i > 0 and str(i)[-1] == "4")

cnt = 0
M = 0

for nums in zip(data, data[1:], data[2:]):
    s = str(nums[0]) + str(nums[1]) + str(nums[2])
    s = s.replace("-", "")
    s = sum(map(int, list(s)))
    if s == m4:
        cnt += 1
        M = max(M, sum(nums))

print(cnt, M)