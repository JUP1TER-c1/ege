from ipaddress import *

cnt = 0
for ip in ip_network('172.16.192.0/255.255.192.0', False).hosts():
    binary = '.'.join([bin(int(byte) + 256)[3:] for byte in str(ip).split('.')])
    if binary.count('1') % 5 != 0:
        cnt += 1
print(cnt)