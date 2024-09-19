count = 0
maxx = 0
file = open('17.txt')
values = [int(i) for i in file]
for i in range(len(values) - 1):
    for j in range(i + 1, len(values)):
        if ((values[i] + values[j]) % 80 == 0) and (values[i] % 50 == 0 or values[j] % 50 == 0):
            count += 1
            maxx = max(maxx, values[i] + values[j])
print(count, maxx)