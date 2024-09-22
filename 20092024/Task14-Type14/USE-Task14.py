def number_to_base(number, base):
    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join(list(map(str, digits[::-1])))

number = 9**8 + 3**5 - 2
print(number_to_base(number, 3))

# Ответ: 4
