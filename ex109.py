def sort_gift_code(code:str):
    return ''.join(sorted(set(code)))
print(sort_gift_code('zyxwvutsrqponmlkjihgfedcba'))