from ipaddress import *

ip1 = ip_address("200.154.190.12")
ip2 = ip_address("200.154.184.0")

for m in range(16, 31):
    net = ip_network(f"{ip1}/{m}", 0)
    if ip1 in net.hosts() and ip2 in net.hosts():
        print(m)