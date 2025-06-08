def redactor(l):
    while '52' in l or '1122' in l or '2222' in l:
        if '52' in l:
            l = l.replace('52', '11', 1)
        if '2222' in l:
            l = l.replace('2222', '5', 1)
        if '1122' in l:
            l = l.replace('1122', '25', 1)
    return l

for n in range(4, 10000):
    if sum([int(digi) for digi in redactor('5' + '2'*n)]) == 64:
        print(n)
        break