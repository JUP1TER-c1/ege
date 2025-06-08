def redactor(l):
    while '1' in l:
        if '10' in l:
            l = l.replace('10', '0001', 1)
        else:
            l = l.replace('1', '000', 1)
    return l

print(redactor('1' + '0'*90).count('0'))