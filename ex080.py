class Winner:

    DECK = {
        '2': 1, '3': 2, '4': 3, '5': 4,
        '6': 5, '7': 8, '8': 9, '9': 10,
        'T': 11, 'J': 13, 'Q': 14, 'K': 15,
        'A': 16
    }

    def __init__(self, deck) -> None:
        self.deck = self.DECK.setdefault(deck) 
        

    def __lt__(self, other):
        if self.deck < other.deck:
            return True
        return False
    
    def __gt__(self, other):
        if self.deck > other.deck:
            return True
        return False

    def __eq__(self, other):
        if self.deck == other.deck:
            return True
        return False    
    
def winner(deckSteve, deckJosh):
    if deckJosh == [] and deckSteve == []:
        return 'Tie'
    win = {'josh': 0, 'steve': 0, 'tie': 0}
    for j, s in zip(deckJosh, deckSteve):
        josh = Winner(j)
        steve = Winner(s)
        if josh > steve:
            win['josh'] += 1
        elif josh < steve:
            win['steve'] += 1
        else:
            win['tie'] += 1
    return f"Steve wins {win['steve']} to {win['josh']}" if win['josh'] < win['steve'] \
        else f"Josh wins {win['josh']} to {win['steve']}" if win['josh'] > win['steve'] \
        else 'Tie'

