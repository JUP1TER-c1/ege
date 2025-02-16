
def verify1(line):
    if line.find('|0') > -1:return False
    elif line.find('|%') > -1:return False
    elif line.find('%|') > -1:return False
    elif line.find('%0') > -1:return False
    elif line.find('0%') > -1:return False
    else:return True

def verify2(line):
    for i in range(1, 154):
        if line.find('|' + '#'*i + '|') > -1: return False
    else: return True


file = open("69932.txt").read()
file = file.replace('-', '%')
file = file.replace('*', '%')
file = file.replace('6', '#')
file = file.replace('7', '#')
file = file.replace('8', '#')
file = file.replace('9', '#')

cache = ['%'*count for count in range(15)][2:]
cache.reverse()
for i in cache:
    file = file.replace(i, '|')

while not verify1(file):
    file = file.replace('|%', '||')
    file = file.replace('%|', '||')

    cache = ['0' * count for count in range(15)][1:]
    cache.reverse()
    for i in cache:
        file = file.replace('|'+i, '||')

    file = file.replace('%0', '|')
    file = file.replace('0%', '|')

file = file.replace('0', '#')

cache = ['#'*count for count in range(1, 154)]
cache.reverse()
while not verify2(file):
    for i in cache:
        file = file.replace('|' + i + '|', '|')

cache = ['|'*count for count in range(1, 40)]
cache.reverse()
while file.find('||') > -1:
    for i in cache:
        file = file.replace(i, '|')

file = file.split('|')
for i in range(len(file)):
    file[i] = len(file[i])

print(max(file))

