def coins(coin1, coin2):
    r = mdc(coin1, coin2)
    if r == 1:
        calculo = (coin1*coin2) - (coin1+coin2)
        return -1 if calculo == 0 else calculo
    return -1
    


def mdc(a, b):
    j = max(a, b)
    
    for i in range(2, j):
        if a % i == 0 and b % i == 0:
            return i
   
    return 1

print(coins(12, 16))