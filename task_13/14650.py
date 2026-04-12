from ipaddress import *

ip1 = ip_address("216.54.187.235")
ip2 = ip_address("216.54.174.128")

for m in range(16, 31):
    net = ip_network(f"{ip1}/{m}", 0)
    if ip1 in net.hosts() and ip2 not in net.hosts():
        print(m)
print("############")
for m in range(16, 31):
    net1 = ip_network(f"{ip1}/{m}", 0)
    net2 = ip_network(f"{ip2}/{m}", 0)
    if net1[0] != net2[0] and ip1 in net1.hosts() and ip2 in net2.hosts():
        print(m)