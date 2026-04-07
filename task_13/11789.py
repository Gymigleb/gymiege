from ipaddress import *

def f(ip):
    ip = f"{int(ip):032b}"
    return ip[:16].count("1") <= ip[16:].count("1")

for a in range(16, 25):
    net = ip_network(f"99.8.254.232/{a}", 0)
    f1 = True
    for i in net:
        if not f(i): 
            f1 = False
            break
    if f1:
        print((a-16))
        print(int("11111000", 2))
        break