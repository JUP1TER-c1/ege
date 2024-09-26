count = 0
max_sum = 0
numbers = [int(number) for number in open('17.txt')]
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j]) % 126 != 0: continue
        count += 1
        max_sum = max(max_sum, numbers[i] + numbers[j])
print(f'Pairs count: {count}\nMax pair sum: {max_sum}')