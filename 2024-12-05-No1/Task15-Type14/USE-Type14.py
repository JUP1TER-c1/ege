for x in '0123456789AB':
    for y in '0123456789AB':
        result = int('8' + x + '78' + y, 12) + int('79' + x + y + '7', 14)
        if result % 99 == 0:
            print(result // 99)