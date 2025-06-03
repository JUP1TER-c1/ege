data = list(map(int, open('17.txt').read().split('\n')))
min_elem = 10**30
for number in data:
    if number > 0 and number % 110 == 0:
        min_elem = min(min_elem, number)
pairs = []
for i in range(len(data) - 1):
    if data[i] + data[i+1] < min_elem:
        pairs.append(data[i] + data[i + 1])
print(len(pairs), max(pairs))
print(pairs)
print(min_elem)