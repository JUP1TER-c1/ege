
data = list(map(int, open('1.txt').read().split('\n')))
res = []
task = 0
for number in data:
    if str(abs(number))[0] == '5' and len(str(abs(number))) == 3:
        task = min(task, number)
for i in range(len(data)-2):
    trio = [data[i], data[i+1], data[i+2]]
    if sum([1 for number in trio if str(number)[-1] == '4']) != 1: continue
    if sum(trio) % task == 0: continue
    res.append(sum(trio))
print(len(res), max(res))