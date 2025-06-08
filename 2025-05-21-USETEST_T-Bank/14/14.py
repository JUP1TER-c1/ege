for x in '0123456789ABCDE':
    eq = int('97968' + x + '15', 15) + int('7' + x + '233', 15)
    if eq % 14 == 0:
        print(eq/14)