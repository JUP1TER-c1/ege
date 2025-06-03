def game(pile1, pile2, step):
    if pile1+pile2 <= 72 or step>4: return step == 4 or step == 2
    moves = [
        game(pile1-3, pile2, step+1),
        game(pile1, pile2-3, step+1),
        game(pile1//2 if pile1%2 == 0 else pile1//2+1, pile2, step + 1),
        game(pile1, pile2//2 if pile2%2 == 0 else pile2//2+1, step + 1)
    ]
    if step%2 == 0:
        return all(moves)
    return any(moves)

print([s for s in range(23, 200) if game(50, s, 0) == True])