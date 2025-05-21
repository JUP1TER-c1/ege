def base10tobase4(n):
    res = ''
    while n>0:
        res += str(n%4)
        n //= 4
    return res[::-1]

maxzeros = 0
for x in range(1, 3001):
    result = base10tobase4(4**210 + 4**110 - x)
    maxzeros = max(maxzeros, result.count('0'))
    if result.count('0') == 105:
        print(x)
print(maxzeros)

