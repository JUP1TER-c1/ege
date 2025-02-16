for x in range(2020+1):
    number = 3**100 - x
    count = 0
    while number!=0:
        if number%3 == 0:
            count += 1
        number = number//3
    if count == 2:
        print(x)
        break