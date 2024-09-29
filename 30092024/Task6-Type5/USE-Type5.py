def process(number):
    bin_number = str(bin(number))[2:]
    if number%2 == 0:
        bin_number = bin_number + '10'
    else:
        bin_number = bin_number + '01'

    return int(bin_number, 2)

for i in range(0, 100000):
    if process(i) <= 102:
        print(process(i))
    else:
        break
