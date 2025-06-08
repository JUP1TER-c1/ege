from itertools import product
res = []
for k in range(1, 4):
    for x in '0123456789':
        for y in product('0123456789', repeat = k):
            number = int('1' + ''.join(y) + '4302' + x + '1')
            if number % 3147 == 0:
                res.append(number)
print(sorted(res))
