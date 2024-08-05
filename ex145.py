# 'B' representam campos com pedras pretas, 
# 'W' representam campos com pedras brancas e
# 'X' representam campos vazios.
board = [
    ['W', 'W', 'W', 'B', 'B', 'B'],
    ['W', 'W', 'W', 'W', 'B', 'B'],
    ['W', 'W', 'W', 'B', 'B', 'B'],
    ['W', 'X', 'W', 'B', 'B', 'B'],
    ['X', 'W', 'B', 'B', 'B', 'B'],
    ['W', 'W', 'B', 'X', 'B', 'X']
]

from collections import Counter

def determine_winner(board:list[list]) -> tuple:
    board = [x for bo in board for x in bo]
    counter = Counter(board)
    return max(filter(lambda x: x[0] != "X", counter.items()), key=lambda v: v[1]) if counter['B'] != counter['W'] else ('T', counter['X']) 

print(determine_winner(board))