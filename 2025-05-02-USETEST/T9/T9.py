data = open('9.txt').readlines()
for line in data:
    line = list(map(int, line.replace('\t', ' ').replace('\n','').split()))
    flags = set(number for number in line if line.count(number) == 3 or line.count(1))
    if len(flags) != 3: continue
    print(flags, line)

