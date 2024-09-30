print('y, x, w, z')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if not ((x and not y) or (y == z ) or w):
                    print(f"{y}, {x}, {w}, {z}")

# Ответ - yxwz
