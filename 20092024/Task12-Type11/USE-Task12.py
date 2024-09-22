line = '1'*78
while line.find('111') > -1:
    line = line.replace('111', '2', 1)
    line = line.replace('222', '11', 1)

print(line)

#Ответ 2211
