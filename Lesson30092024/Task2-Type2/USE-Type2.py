print('x, z, w, y')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if not (((w <= x) or (y <= z)) and ((x == y) <= (w == z))):
                    print(f"{x}, {z}, {w}, {y}")

# Ответ - xzwy
