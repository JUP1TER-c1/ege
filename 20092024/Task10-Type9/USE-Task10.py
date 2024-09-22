count = 0
for line in open('09.txt'):
    row = [int(number) for number in line.split()]
    if len(row) > 0:                               #По некоторой причине в файле содержатся пустые строки и повреждённые символы
        if row.count(min(row)) == 1:
            if len(row) > len(set(row)):
                avg = ((sum(row) - max(row))/5)*3
                if max(row) > avg:
                    count+=1
print(count) #Ответ: 49