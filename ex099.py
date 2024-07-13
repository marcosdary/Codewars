def sum_dig_pow(a, b):
    dig = []
    for x in range(a, b+1):
        y = str(x)
        num = sum(pow(int(y[i]), i+1) for i in range(0, len(y)))
        if num == x:
            dig.append(x)
    return dig

print(sum_dig_pow(1, 10))