def base10to3(n):
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

for x in range(2031):
    if base10to3(3**100 - x).count('0') == 1:
        print(x)