file = list(open('26.txt').readlines())
max_disk, users = list(map(int, file.pop(0).split()))
data = sorted(list(map(int, file)))

amounts = {item:data.count(item) for item in set(data)}

disk = []
while sum(disk) <= max_disk - min(data):
    disk.append(data.pop(0))

opt_disk = disk[:-1]
for candidate in data[::-1]:
    opt_disk.append(candidate)
    if sum(opt_disk) <= max_disk:
        print(candidate)
    else:
        opt_disk.pop(-1)


print(len(disk), max(disk))