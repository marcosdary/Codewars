from functools import reduce

def valid_ISBN10(isbn:str): 
    if len(isbn) != 10:
        return False
    
    T = len(isbn)
    s = 0
    if isbn[-1] == "X":
        s += 10 * 10
        T = len(isbn) - 1
    
    for i in range(0, T):
        
        if isbn[i] == 'X' or isbn[i].isalpha():
            return False
        s += int(isbn[i]) * (i+1)


    return True if s % 11 == 0 else False

print(valid_ISBN10('96667720278')) # False