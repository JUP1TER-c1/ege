def operate(line):
    line = str(line)
    while line.find('333') > -1 or line.find('777') > -1:
        if line.find('333') > -1:
            line = line.replace('333', '7', 1)
        else:
            line = line.replace('777', '3', 1)
    return line

input_line = '7'*85
print(operate(input_line))
#Ответ: 8811