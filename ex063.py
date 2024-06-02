def zeros(max_num):
    tot_zero = 0
    count = -1
    i = 1
    while count != 0:
        count = max_num // pow(5, i)
        tot_zero += count
        i += 1
    return tot_zero  
print(zeros(1000000000))
