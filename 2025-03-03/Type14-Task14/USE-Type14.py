def base10to6(n):
    res = ''
    res += str(n % 6)
    while n>=6:
        n = n//6
        res += str(n % 6)
    return res[::-1]

print(base10to6(36**7 + 6**19 - 18).count('0'))
