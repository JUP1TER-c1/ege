from math import *

max_weight = 33*1024*1024 # bytes
for power in range(2, 8193):
    bit_per_symbol = ceil(log2(power))
    byte_per_tag = ceil((257*bit_per_symbol)/8)
    tags_weight = 295740 * byte_per_tag
    if tags_weight < max_weight:
        print(power)
