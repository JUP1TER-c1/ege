def game(p1, p2, step):
    if p1 + p2 >= 59: return step % 2 == 0
    if step == 0: return 0
    outcomes = [game(p1 + 1, p2, step - 1), game(p1 * 2, p2, step - 1), game(p1, p2 + 1, step - 1), game(p1, p2 * 2, step - 1)]
    return any(outcomes) if step % 2 == 1 else any(outcomes)

print('19', [s for s in range(1, 54) if game(5, s, 2)])