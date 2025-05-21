from ipaddress import *

net = ip_network("172.16.80.0/255.255.248.0", False).hosts()

cnt = 0
for ip in net:
    ones = f"{int(ip):b}".count('1')
    if ones % 2 == 1:
        cnt += 1
print(cnt)

