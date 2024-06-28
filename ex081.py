def persistence(num, s = 0):
    if isinstance(num, int):
        num = str(num)

    if len(num) == 1:
        return 0
    
    r = 1
    for i in range(0, len(str(num))):
        r *= int(str(num)[i])

    num = str(r)
    s += 1

    if len(num) == 1:
        return s
    
    return persistence(num, s)
print(persistence(999))