def play(stones, step, end_steps):
    if stones <= 17:
        return step in end_steps
    if step >= max(end_steps):
        return 0
    outcomes = [play(stones - 5, step + 1, end_steps)]
    if stones % 2 == 0:
        outcomes.append(play(stones // 2, step + 1, end_steps))
    if stones % 3 == 0:
        outcomes.append(play(stones // 3, step + 1, end_steps))
    else:
        outcomes.append(play(stones + 1, step + 1, end_steps))
    if step % 2 == max(end_steps) % 2:
        return all(outcomes)
    else:
        return any(outcomes)


for init_stones in range(17, 10000):
    if play(init_stones, 0, [2, 4]) == 1 and play(init_stones, 0, [2]) == 0:
        print(init_stones)