def find_divisors(n):
    base = int(max(((n // 2) + i) for i in range(1, 11) if ((n // 2) + i) % 10 == 7))
    res = []
    for c in range(base, 16, -10):
        if n % c == 0:
            res.append(c)
    return res

result = []
mark = 1125000
while len(result) < 5:
    divisors = find_divisors(mark)
    if len(divisors) > 0:
        result.append([mark, min(divisors)])
    mark+=1

print(result)