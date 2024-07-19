from re import sub, I, findall, search, compile

def coffee(sentence):
    
    return sub(r'Coffee', 'COFFEE', sentence, flags=I)

