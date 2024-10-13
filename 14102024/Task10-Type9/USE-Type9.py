count = 0
for line in open('09.txt'):
    row = [int(number) for number in line.split()]
    if len(row) == len(set(row)): # — все числа в строке различны;
        even = [number for number in row if number % 2 == 0]
        odd = [number for number in row if number % 2 != 0]
        if len(odd) > len(even):
            if sum(odd) < sum(even):
                count += 1
print(count)