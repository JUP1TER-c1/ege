def f(line):
    while '111' in line:
        line = line.replace('111', '2', 1)
        line = line.replace('222', '11', 1)
        line = line.replace('1', '2', 1)
    return line


for number in range(1, 101):
    line =  f('1'*number)
    if line.count('2') == len(line):
        print(f'Количество единиц: {number}\nРезультат: {line}\n')

count = 0
for i in range(123456794, 678901234):
    if i%16 == 0 or i%16 == 9 or i%16 == 10:
        count+=1
print(count)