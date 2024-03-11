from math import sqrt

def goldbach_partitions(n):
    if is_prime(n) or n == 15:
        return []
    
    
    combinations_numbers =  list()
    for i in range(1, n+1):
        if (n-i) == i:
            combinations_numbers.append((i, i))
        elif (n-i) > i:
            combinations_numbers.append((i, n-i))
    
    result_cousins = filter(lambda x: is_prime(x[0]) and is_prime(x[1]) and sum(x) == n, combinations_numbers)
    
    return formatted_version(result_cousins)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def formatted_version(values):
    list_values = list()
    for number in values:    
        s = f'{number[0]}+{number[1]}'   
        list_values.append(s)
    return list_values
    
       

print(goldbach_partitions(15))  

