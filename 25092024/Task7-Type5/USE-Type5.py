for number in range(10000, 999, -1):
    number = str(number)
    part1 = int(number[0]) + int(number[1])
    part2 = int(number[1]) + int(number[2])
    part3 = int(number[2]) + int(number[3])
    parts = [part1, part2, part3]
    parts.remove(min(parts))
    result = str(min(parts)) + str(max(parts))

    if result == '1315':
        print(number)
        break

#Ответ: 168