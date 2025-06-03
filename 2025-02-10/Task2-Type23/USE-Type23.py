from itertools import product

def solution(number, target):
    if number > target:
        return 0
    elif number == target:
        return 1
    else:
        return solution(number + 1, target) + solution(number + 2, target) + solution(number + 3, target)

    
def decrypt(number, sequence):
    steps = [number]
    for key in sequence:
        if key == '1':
            number += 1
            steps.append(number)
        elif key == '2':
            number += 2
            steps.append(number)
        elif key == '5':
            number += 3
            steps.append(number)
        if number >= 38:
            break
    return steps

# count=0
# for i in range(1, 28):
#     sequences = product(('1', '2', '5'), repeat=i)
#     for sequence in sequences:
#         steps = decrypt(7, sequence)
#         if (7 in steps) and (steps[-1] == 35):
#             count += 1
# print(count)
print(solution(1, 7) * solution(7, 35))
# 23