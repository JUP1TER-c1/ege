count = 0
max_pair = 0
file = open('17.txt')
numbers = [int(entry) for entry in file]
for i in range(len(numbers) - 1):
    for j in range(i+1, len(numbers)):
        if (numbers[i] + numbers[j] % 2 == 1) and (numbers[i] * numbers[j] % 5 == 0):
            count += 1
            max_pair = max(max_pair, numbers[i]+numbers[j])
print(count, max_pair)
