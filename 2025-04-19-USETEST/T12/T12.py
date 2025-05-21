def redactor(n):
    while '42' in n or '8222' in n or '2222' in n:
        if '42' in n:
            n = n.replace('42', '2', 1)
        if '8222' in n:
            n = n.replace('8222', '24', 1)
        if '2222' in n:
            n = n.replace('2222', '8', 1)
    return n

for i in range(3, 10000):
    result = redactor('4' + '2'*i)
    summ = 0
    for num in result:
        summ += int(num)
    if summ == 110:
        print(i)