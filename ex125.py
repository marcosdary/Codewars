def friend(x:list):
    return list(filter(lambda a: len(a) == 4, x))

print(friend(["Ryan", "Kieran", "Mark",])) # ["Ryan", "Mark"]