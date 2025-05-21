def get_divisors(number):
    result = [1, number]
    for candidate in range(2, (number//2) + 1):
        if number % candidate == 0:
            result.append(candidate)
    return sorted(result)

def calculator(current, end):
    if current > end: return 0
    if current == end: return 1
    return calculator(current + 1, end) + calculator(sum(get_divisors(current)), end)

print(calculator(2, 24))