from itertools import *
def base7to10(number):
    result = 0
    for i in range(len(number)):
        result += int(number[i])*(7**(len(number) - i - 1))
    return result
def base9to10(number):
    result = 0
    for i in range(len(number)):
        result += int(number[i])*(9**(len(number) - i - 1))
    return result

acceptable_numbers = '0123456'
minn = 1_000_000_000
for x, y in permutations(acceptable_numbers, r=2):
    cache = base7to10(y + x + '320') + base9to10('1' + x + '3' + y + '3')
    if cache % 181 != 0: continue
    minn = min(cache, minn)

print(minn / 181)
