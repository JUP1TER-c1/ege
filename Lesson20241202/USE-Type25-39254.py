count = 0
number = 500_000_001
while count < 5:
    M = 1
    divider_count = 0
    for i in range(2, number//2):
        if number%i==0:
            divider_count += 1
            M *= i
            if divider_count == 5: break
    if divider_count == 5 and M < number:
        count += 1
        print(f'Number = {number}\nM = {M}\n')
    number += 1
