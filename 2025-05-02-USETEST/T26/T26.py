boxes = sorted(list(map(int, open('26.txt').read().split('\n'))))[::-1]
cnt = 0
last_box = boxes[0]
line = [last_box]
for box in boxes:
    if last_box - box >= 9:
        last_box = box
        line.append(box)
        cnt += 1
print(cnt)
print(min(line))
