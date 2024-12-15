cache = []
for x in range(20,0,-1):
    for y in range(20,0,-1):
        for z in range(20,0,-1):
            number = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in number:
                number = number.replace('01', '220', 1)
                number = number.replace('02', '1013', 1)
                number = number.replace('03', '120', 1)
            if number.count('1') == 13 and number.count('2') == 18:
                cache.append(x + y + z)
print(max(cache) + 2)