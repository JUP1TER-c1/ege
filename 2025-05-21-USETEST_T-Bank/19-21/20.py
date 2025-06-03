def game(pile1, pile2, move):
    print(f"Game state:\n Pile1 = {pile1}\n Pile2 = {pile2}\n Move = {move}\n\n")
    if pile1 + pile2 >= 231: return move % 2 == 0
    if move == 0: return 0
    states = [game(pile1 + 1, pile2, move - 1), game(pile1 * 2, pile2, move - 1), game(pile1, pile2 + 1, move - 1), game(pile1, pile2 * 2, move - 1)]
    return any(states) if (move - 1) % 2 == 0 else all(states)

print([s for s in range(1, 214) if not game(17, s, 2) and game(17, s, 4)])