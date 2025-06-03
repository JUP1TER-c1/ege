def base10to7(n):
    res = ''
    while n > 0:
        res = str(n % 7) + res
        n //= 7
    return res
max_zeros = 0
for x in range(1, 2031):
    equation = base10to7(7**170 + 7**100 - x)
    zeros = equation.count("0")
    #print(zeros, max_zeros)
    if zeros >= max_zeros:
        max_zeros = zeros
        print(x)

print(base10to7(7**170 + 7**100 - 1715))