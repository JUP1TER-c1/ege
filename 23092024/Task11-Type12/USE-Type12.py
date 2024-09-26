def operate(line):
    line = str(line)
    while line.find('11111') > -1 or line.find('888') > -1:
        if line.find('11111') > -1:
            line = line.replace('11111', '88', 1)
        elif line.find('888') > -1:
            line = line.replace('888', '8', 1)
    return line

input_line = '1'*82
print(operate(input_line))
#Ответ: 8811