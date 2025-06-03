line = ["9" for i in range(127)]
line = ''.join(line)

while ('333' in line) or ('999' in line):
    if ('333' in line):
        line = line.replace('333', '9',1)
    else:
        line = line.replace('999', '5', 1)

print(line)