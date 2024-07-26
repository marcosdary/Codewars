def is_isogram(string:str):
    string = string.lower()
    for i in range(0, len(string)):
    
        if string.count(string[i]) > 1:
            return False
    return True
print(is_isogram('isIsogram'))
