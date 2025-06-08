from ipaddress import *

cnt = 0
for ip in ip_network('172.16.80.0/255.255.248.0', False):
    binIP = '.'.join(bin(int(byte) + 256)[3:] for byte in str(ip).split('.'))
    if binIP.count('1') % 2 == 1:
        cnt += 1
print(cnt)
