data = [int(x) for x in open('17.txt')]

def check(number):
    return 1000<=abs(number)<10000 and abs(number)%10 == 6

min_number = min(number for number in data if number>0 and check(number))
result = []
count = 0
maxsum = 0
for x, y, z in zip(data, data[1:], data[2:]):
    if check(x) + check(y) + check(z) == 1 and x+y+z <= min_number:
        result.append(x+y+z)
print(len(result), max(result))