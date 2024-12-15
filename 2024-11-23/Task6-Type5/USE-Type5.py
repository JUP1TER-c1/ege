cache = [False] * 1_000_000
for number in range(1, 10_000):
    bin_number = bin(number)[2:] + bin(number%4)[2:]
    result = int(bin_number, 2)
    cache[result] = True

max_row = 0
for index in range(10_000):
    max_row = max(max_row, sum(cache[index:index+65]))

print(max_row)