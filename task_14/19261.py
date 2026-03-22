from string import printable

def f(arr):
    arr = arr[::-1]
    out = 0
    for i in range(len(arr)):
        out += arr[i]*37**i
    return out

for x in range(0,36):
    a = f([9, 8, x, 3, 1])
    b = f([1, x, 9, 2, 4])
    if (a + b) % 21 == 0:
        print(x, (a+b)//21)