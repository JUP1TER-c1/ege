def is_prime(number):
    for divider in range(2, int(number**0.5)+1):
        if number % divider == 0:
            return False
    return True

def redactor(line=''):
    while '01' in line or '02' in line:
        line = line.replace('02', '1110', 1)
        line = line.replace('01', '220', 1)
    return line

minn = 100500
for ones in range(100):
    for twos in range(100):
        A = '0' + '1' * ones + '2' * twos
        if len(A) <= 44: continue
        B = redactor(A)
        if is_prime(B.count('1') + B.count('2')*2):
            minn = min(minn, ones + twos*2)

print(minn)