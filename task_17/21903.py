with open("./files/17_21903.txt") as f:
    data = [int(i) for i in f]
    M15 = min(i for i in data if len(str(abs(i))) == 3 and str(i)[-2:] == "15")**2

cnt = 0
m = 10**100

for nums in zip(data, data[1:], data[2:]):
    u1 = str(nums[0]).count("-") == str(nums[1]).count("-") == str(nums[2]).count("-")
    if u1 and min(nums) * max(nums) > M15:
        cnt += 1
        m = min(m, min(nums) * max(nums))

print(cnt, m)