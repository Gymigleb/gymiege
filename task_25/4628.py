from fnmatch import fnmatch

for i in range(124065 - 124065%161, 10**8+1, 161):
    if fnmatch(str(i), "12*4?65") and i%161 == 0:
        print(i, i//161)