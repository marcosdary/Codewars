from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def twin_prime(n):
    s = 0
    for i in range(1, n):
        if is_prime(i) and is_prime(i+2):
            s += 1   
    return s
