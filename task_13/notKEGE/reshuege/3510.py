from ipaddress import *

net = ip_network("217.9.142.131/255.255.192.0", 0)

print(net[0], "HBEA")