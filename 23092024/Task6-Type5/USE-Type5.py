for number in range(100, 1001):
    number = str(number)
    part1 = int(number[0]) + int(number[1])
    part2 = int(number[1]) + int(number[2])
    result = str(min(part1, part2)) + str(max(part1, part2))

    if result == '714':
        print(number)
        break

#Ответ: 168
