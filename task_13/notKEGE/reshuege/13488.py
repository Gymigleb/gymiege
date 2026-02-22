from ipaddress import *

for m in range(1, 33):  
    net = ip_network(f"119.83.200.27/{m}", 0)
    if str(net[0]) == "119.83.192.0":
        print(m)
    for i in net: pass