from itertools import product

def decrypt(number, sequence):
    steps = [number]
    for key in sequence:
        if key == 'A':
            number -= 2
            steps.append(number)
        elif key == 'B':
            number //= 2
            steps.append(number)
    return steps

count=0
for i in range(1, 19):
    sequences = product(('A', 'B'), repeat=i)
    for sequence in sequences:
        steps = decrypt(38, sequence)
        if (16 in steps) and (steps[-1] == 2):
            count += 1
print(count)