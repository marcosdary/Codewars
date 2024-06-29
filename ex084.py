LETTER = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 
    'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
    'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def rank(st, we, n):
    st = st.split(',')

    if st == []:
        return 'No participants'
    if n > len(st):
        return 'Not enough participants'
    
    winning_numbers = {}
    for index, word in enumerate(st):
        s = 0
        for letter in word:
            s += LETTER[letter.upper()]
        winning_numbers[word] = (len(word) + s) * we[index]

    sort_ = sorted(winning_numbers.items(), key=lambda x: (-x[1], x[0]))
    return [name for name, som in sort_][n-1]
    
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))



