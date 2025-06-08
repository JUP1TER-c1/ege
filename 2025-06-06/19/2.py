def game(pile, step):
    if pile <= 21: return step % 2 == 0
    if step == 0: return 0
    outcomes = [game(pile - 3, step - 1), game(pile - 7, step - 1), game(pile//4, step - 1)]
    return any(outcomes) if step % 2 == 1 else all(outcomes)

print('19', [s for s in range(22, 1000) if not game(s, 1)])