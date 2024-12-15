from itertools import *

even = '2468'
odd = '1357'
count = 0
for number in product(even, odd, even, odd, even, odd, even, odd, even, odd, even):
    cache = ''.join(number)
    for digit in range(1, 9):
        if cache.count(str(digit)) > 4:
            break
    else:
        count += 2

print(count)