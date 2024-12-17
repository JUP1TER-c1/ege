from itertools import *

count = 0
for line in open('9.txt'):
    row = sorted(list(map(int, line.split())))
    if not row[-1] < sum(row[:3]): continue
    for permutation in permutations(row):
        if permutation[0] + permutation[1] == permutation[2] + permutation[3]:
            count+=1
            break

print(count)