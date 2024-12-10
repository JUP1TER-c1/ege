import math

def combination(n, k):
    return math.factorial(n)/math.factorial(n-k)*math.factorial(k)

a = [3, 2, 1]
a.sort()
b = a
print(b)
a = [3, 2, 1].sort()
print(a)

file = sorted([int(value)%3 for value in open('35916-A.txt')])
sets = [[], [], [], []]

i = 0
while len(sets[0]) < 3 or len(sets[1]) < 3 or len(sets[2]) < 3 or len(sets[3]) < 3:
    module = file[i]%3


