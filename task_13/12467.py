from ipaddress import *

for a in range(256):
    net = ip_network(f"183.192.{a}.0/255.255.252.0", 0)
    f1 = True
    for i in net:
        bin_i = f"{int(i):032b}"
        if bin_i[16:].count("1") <= 3:
            f1 = False
            break
    if f1:
        print(a)
        break