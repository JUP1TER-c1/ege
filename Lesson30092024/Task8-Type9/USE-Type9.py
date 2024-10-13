file = open('USE-Type9')
data = []
for line in file:
    row = list(map(int, line.split()))
    data.append(row)
file.close()

def count_appearances(number):
    result = 0
    for row in data:
        result += row.count(number)
    return result

count = 0
for row in data:
    for number in row:
        if count_appearances(number) == 50:
            if row.count(number) == 1:
                count += 1

print(count)