def number_to_base(number, base):
    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join(list(map(str, digits[::-1])))

for number in range(100000):
    number = str(number)
    if len(number) != 11: continue
    if (number.count('1') + number.count('5') + number.count('5') + number.count('7') + number.count('9')) != 3: continue
    