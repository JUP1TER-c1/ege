
def operate(number, command):
    if command == 'A':
        return number - 1
    elif command == 'B':
        return number * 2
    elif command == 'C':
        return number * 3
    elif command == '':
        return number

def solution(number, target, command):
    number = operate(number, command)
    #print(number, command)
    if number > target+1:
        return 0
    elif number == target:
        return 1
    elif command == 'A':
        return solution(number, target, 'B') + solution(number, target, 'C')
    else:
        return solution(number, target, 'A') + solution(number, target, 'B') + solution(number, target, 'C')

print(solution(3, 15, ''))
