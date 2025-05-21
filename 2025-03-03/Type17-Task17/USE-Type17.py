# print([int(n == 1 or(n==9)) for n in range(10)])
file = list(map(int,open("17.txt").read().split()))
count = 0
m = 0
for i in range(len(file) - 1):
    for j in range(i + 1, len(file)):
        if (file[i] - file[j]) % 2 == 0 and (file[i] % 31 == 0 or file[j] % 31 == 0):
            count += 1
            m = max(m, file[i] + file[j])
print(count, m)

# (((list(map(int,open("17.txt").read().split()))[i]-list(map(int,open("17.txt").read().split()))[j])%2==0)and((list(map(int,open("17.txt").read().split()))[i]%31==0)or(list(map(int,open("17.txt").read().split())) % 31 == 0)))
# print(sum([(((file[i]-file[j])%2==0)and((file[i]%31==0)or(file[j] % 31 == 0))) for i, j in [([i1, j1] for j1 in range(i1+1, len(file))) for i1 in range(len(file)-1)]]))

# print([[i1, j1] for j1 in range(i1+1, len(list(map(int,open("17.txt").read().split())))) for i1 in range(len(list(map(int,open("17.txt").read().split())))-1)])
# print(sum([sum([bool(i > 5 and j == 9) for j in range(i + 1, 10)]) for i in range(10-1)]))
# count = 0
# for i in range(10 - 1):
#     for j in range(i + 1, 10):
#         if i > 5 and j == 9:
#             count += 1
# print(count)

# print(sum([sum([bool((((file[i]-file[j])%2==0)and((file[i]%31==0)or(file[j]%31==0)))) for j in range(i+1,len(file))]) for i in range((len(file)-1))]))
#
#
#
#
#
#
#
# print(max([max([file[i] + file[j] for j in range(i+1,len(file)) if bool((((file[i]-file[j])%2==0)and((file[i]%31==0)or(file[j]%31==0))))]) for i in range((len(file)-1))]))
