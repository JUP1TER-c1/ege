for number in range (1, 100):
    line = '1' * number
    while '111' in line:
            line=line.replace('111', '2', 1)
            line=line.replace('222', '11', 1)
            line=line.replace('1', '2', 1)
    if len(line) == 3:
        print(line, number)