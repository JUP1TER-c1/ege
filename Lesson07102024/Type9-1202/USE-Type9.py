inputs = ['56789', '85758', '77700', '50786']
for number in inputs:
    for digit in ['5', '6', '8']:
        if number[0] != digit or number[-1] == digit: continue
        for mid_digit in ['5', '7', '8']:
            if number[len(number)//2] == mid_digit and number[0] != mid_digit:
                if int(number)%2 == 0:
                    print(number)


