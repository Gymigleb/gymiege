with open("./325_26.txt") as f:
# with open("./small.txt") as f:
    n, m, k = list(map(int, f.readline().split()))
    a=m
    m=k
    k=a
    matrix = [[0 for i in range(k)] for j in range(m)]
    for i in f:
        y, x = list(map(int, i.split()))
        matrix[x-1][y-1] = 1

def f(arr):
    ones = [-1]
    out = []
    for i in range(len(arr)):
        if arr[i] == 1:
            ones.append(i)
    ones.append(len(arr))
    # print(ones)
    for i in range(len(ones) - 1):
        out.append((ones[i+1] - ones[i] - 2, ones[i+1] - 1))
    # print(out)
    return max(out, key=lambda x: (x[0], -x[1]))

# arr = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]
# print(f(arr))

# for i in range(m):
#     print(*matrix[i])

ans = []
for i in range(m):
    ans.append(f(matrix[i]))
    # print(ans[-1])
print(max(ans, key=lambda x: (x[0], -x[1]))[0]+1, max(ans, key=lambda x: (x[0], -x[1]))[1])