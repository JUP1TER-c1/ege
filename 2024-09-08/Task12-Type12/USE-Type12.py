for number in range(3, 10000 + 1):
    line = '5' + '2' * number
    while ('52' in line) or ('1122' in line) or ('2222' in line):
        line = line.replace('52', '11', 1)
        line = line.replace('2222', '5', 1)
        line = line.replace('1122', '25', 1)
    if line.count("1")+2*line.count("2")+5*line.count("5") == 64:
        print(number)
        break