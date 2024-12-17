from itertools import *

count=0
for permutation in permutations('0234567', r=5):
    number = ''.join(permutation)
    for i in range(len(number) - 1):
        if (int(number[i])%2 == 0 and int(number[i+1])%2 == 0) or (int(number[i])%2 == 1 and int(number[i+1])%2 == 1):
            break
    else:
        if number[0] != '0':
            count += 1

print(count)