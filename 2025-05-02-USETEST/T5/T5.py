def algo(N):
    R = bin(N)[2:]
    digit_sum = sum(int(digit) for digit in R)
    if digit_sum % 2 == 0:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    return int(R, 2)

for N in range(1000):
    if algo(N) > 480:
        print(N)
        break