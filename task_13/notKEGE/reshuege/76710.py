from ipaddress import *

print(*[f"{i:08b}" for i in (130, 0, 5, 80)])
m = 6 + 8 * 2
print(m)

net = ip_network("130.0.5.80/22", 0)
cnt = 0

for i in net:
    s = f"{i:b}"
    # print(s)
    if s[m:].count("1") == 3:
        cnt += 1
print(cnt)