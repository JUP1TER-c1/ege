line = '8' * 99 + '1'
while ('133' in line) or ('881' in line):
    if '133' in line:
        line = line.replace('133', '81', 1)
    else:
        line = line.replace('881', '13', 1)
print(line)