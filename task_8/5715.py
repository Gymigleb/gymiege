alph = ["cookie", "candy", "bar", "nothing"]

def t(s):
    if s.count("candy") > s.count("cookie") > s.count("bar"): return True
    return False

cnt = 0

for cookie in range(0,15):
    for candy in range(0,15):
        for bar in range(0,15):
            s =  "cookie " * cookie + "candy " * candy + "bar " * bar
            s = s.split()
            if len(s) <= 15 and t(s):
                cnt += 1

print(cnt)