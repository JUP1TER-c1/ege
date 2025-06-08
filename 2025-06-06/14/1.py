for x in '012345678':
    for y in '012345678':
        num1 = int('88' + x + '4' + y, 9)
        num2 = int('7' + x + '44' + y, 11)
        expr = num1 + num2
        if expr % 61 == 0:
            print(expr / 61)
            break