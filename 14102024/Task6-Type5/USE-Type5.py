def f(number):
    bin_number = bin(number)[2:]
    bin_number = bin_number[:-1]
    if number%2 == 1:
        bin_number = bin_number + '10'
    else:
        bin_number = bin_number + '01'
    return int(bin_number, 2)

for N in range(2, 100001):
    if f(N) == 2018:
        print(N)