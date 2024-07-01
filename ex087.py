def unique_in_order(sequence):
    repeat_sequence = []
    if isinstance(sequence, list):
        n = sequence[0]
        repeat_sequence.append(n)
        for x in sequence:
            if x != n:
                n = x
                repeat_sequence.append(n)
        return repeat_sequence
    sequence = list(sequence)
    s = sequence[0]
    repeat_sequence.append(s)
    for x in sequence:
        if x != s:
            s = x
            repeat_sequence.append(s)
    return repeat_sequence
string = 'AAAABBBCCDAABBB'
numbers = [1, 2, 2, 3, 3]
print(unique_in_order(string)) # ['A', 'B', 'C', 'D', 'A', 'B']