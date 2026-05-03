from fnmatch import fnmatch

mask = "89*6?7?9?"

for i in range(9874, 10**10 + 1, 9874):
    if fnmatch(str(i), mask):
        print(i, i//9874)