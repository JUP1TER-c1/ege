from math import *
for alph in range(2, 2048):
    symbol_bit = ceil(log2(alph))
    tag_byte = ceil((symbol_bit*248)/8)
    tags_byte = tag_byte * 75600
    if tags_byte > 16*1024*1024:
        print(alph)
        break