data = open('26.txt')
N, M, K = list(map(int, data.readline().split()))
min_occupied_row_per_seat = [M+1] * K

for i in range(N):
    row, seat = list(map(int, data.readline().split()))
    min_occupied_row_per_seat[seat - 1] = min(min_occupied_row_per_seat[seat - 1], row)

seats_per_row = dict()
for i in range(M+1):
    seats_per_row[i+1] = []
for i in range(len(min_occupied_row_per_seat)):
    seats_per_row[min_occupied_row_per_seat[i]].append(i+1)
for i in range(M+1):
    seats_per_row[i+1] = sorted(seats_per_row[i+1])

for i in range(M+1, 1, -1):
    row = sorted(seats_per_row[i])
    for j in range(len(row) - 1):
        if row[j] == row[j+1] - 1:
            print(i - 1, row[j])
            break
    for item in row:
        seats_per_row[i-1].append(item)



for i in range(K-1):
    pass
