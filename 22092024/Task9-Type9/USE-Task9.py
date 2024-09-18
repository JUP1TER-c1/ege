count = 0
for line in open('09.txt'):
    row = [int(number) for number in line.split()]
    repeating = [value for value in row if row.count(value) > 1]
    non_repeating = [value for value in row if row.count(value) == 1]
    if len(non_repeating) > 0 and len(repeating) > 0:
        if (sum(non_repeating) / len(non_repeating)) > (sum(repeating) / len(repeating)):
            count += 1
print(count) #Ответ: 2102