from math import *

for n in range(500000):
    tag_size_bit = n*ceil(log2(963 + 10 + 52))
    tag_size_byte = ceil(tag_size_bit/8)
    if 2000 * tag_size_byte <= 693*1024:
        print(n)
