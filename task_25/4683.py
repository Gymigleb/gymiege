from fnmatch import fnmatch

for i in range(2123406-2123406%37, 10**8+1, 37):
    if fnmatch(str(i), "2*1234?6"):
        print(i, i//37)