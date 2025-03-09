import math
from itertools import permutations, product


def combination(n, k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

digits = '123456789'
letters = 'ABCDE'

cache = []
for i in range(1, 5):
    cache.append(len(list(product(digits, repeat = 6-i)))*len(list(product(letters, repeat=i)))*combination(5 , i)*combination(7, 2))

print(sum(cache))
print(combination(8, 2))
