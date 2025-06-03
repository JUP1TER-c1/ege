from ipaddress import *

from unicodedata import normalize


def dotted_decimal_to_CIDR(dotted_decimal):
    return bin(int(ip_address(dotted_decimal)))[2:].count('1')

mask = dotted_decimal_to_CIDR('255.255.255.252')
print(ip_network(f'95.31.171.89/{mask}', 0))


for mask in range(33):
    network = ip_network(f'224.128.112.142/{mask}', False)
    print(network.network_address)
    if str(network.network_address) == "224.128.64.0":
        res = str(IPv4Address(int(("1" * mask).ljust(32, "0"), 2)))
        print(res.split(".")[2])