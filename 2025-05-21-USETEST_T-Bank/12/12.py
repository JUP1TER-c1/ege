def redactor(line):
    while '33333' in line or '777' in line:
        if '33333' in line:
            line = line.replace('33333', '7', 1)
        if '777' in line:
            line = line.replace('777', '3', 1)
    return line

print(redactor('7'*108))