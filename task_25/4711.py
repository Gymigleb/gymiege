from fnmatch import fnmatch

for i in range(1021394 - 1021394%2023, 10**10+1, 2023):
    if fnmatch(str(i), "1?2139*4"):
        print(i, i//2023)