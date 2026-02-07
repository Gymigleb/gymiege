from fnmatch import fnmatch

for i in range(0, 10**10 + 1, 2023):
    if fnmatch(str(i), "1?1?1?1*1") and sum(map(int, str(i))) == 22:
        print(i)