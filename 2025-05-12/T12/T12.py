def redactor(line):
    while '19' in line or '399' in line or '999' in line:
        if '19' in line:
            line = line.replace('19', '9', 1)
        if '399' in line:
            line = line.replace('399', '91', 1)
        if '999' in line:
            line = line.replace('999', '3', 1)
    return line

for n in range(4, 10000):
    inline = '1' + '9'*n
    result = sum(int(digit) for digit in redactor(inline))
    if result == 33:
        print(n)
        break