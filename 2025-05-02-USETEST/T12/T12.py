def redactor(line):
    while '31' in line or '211' in line or '1111' in line:
        if '31' in line:
            line = line.replace('31', '1', 1)
        if '211' in line:
            line = line.replace('211', '13', 1)
        if '1111' in line:
            line = line.replace('1111', '2', 1)
    return line


for n in range(3, 10001):
    res = redactor('5' + ('1' * n))
    if sum(int(d) for d in res) == 15:
        print(n)
        break


