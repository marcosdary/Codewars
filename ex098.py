def rps(p1, p2):
    condicoes = {'paper': 'rock', 'rock': 'scissors', 'scissors': 'paper'}

    if p1 == p2:
        return 'Draw!'
    if condicoes.get(p1) == p2:
        return "Player 1 won!"
    return "Player 2 won!"
    
print(rps('rock', 'scissors')) #"Player 1 won!"