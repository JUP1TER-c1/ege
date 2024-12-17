def redactor(line=''):
    while ('52' in line) or ('1122' in line) or ('2222' in line):
        if '52' in line:
            line = line.replace('52', '11', 1)
        if '2222' in line:
            line = line.replace('2222', '5', 1)
        if '1122' in line:
            line = line.replace('1122', '25', 1)
    return line

for n in range(1000):
    gen_line = redactor('5' + '2' * n)
    if gen_line.count('5')*5 + gen_line.count('2')*2 + gen_line.count('1') == 64:
        print(n)
        break