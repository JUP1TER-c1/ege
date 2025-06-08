def game(pile, step):
    if pile >= 67: return step % 2 == 0
    if step == 0: return 0
    outcomes = [game(pile + 1, step - 1), game(pile + 4, step - 1), game(pile * 3, step - 1)]
    return any(outcomes) if step % 2 == 1 else all(outcomes)

print('19', [s for s in range(1, 67) if game(s, 2)])