# e = 2,7182818284
# modelo Simpson
# P (x) = lamb**x * e**-lamb /  x !
from math import factorial

def prob_simpson(lamb, x, op='='):
    e =  2.7182818284 #2.7182818285
    
    if  op == '=':
        p = lambda a, b: (a**b * e ** -a)/factorial(b)
        return p(lamb, x)
     
    return cumulative_probability(lamb, x, op)
    

def cumulative_probability(a, b, c):
    e = 2.7182818284
    if c == '<':
        numbers = list(range(b))
        sum_probability = map(lambda i: (a**i * e **(-a))/factorial(i), numbers)
        return sum(sum_probability)
    
    elif c == '<=':
        numbers = list(range(b+1))
        sum_probability = map(lambda i: (a**i * e **(-a))/factorial(i), numbers)
        return sum(sum_probability)
    
    elif c == '>':
        numbers = list(range(b+1))
        sum_probability = map(lambda i: (a**i * e **(-a))/factorial(i), numbers)
        return 1 - sum(sum_probability)
    
    else:
        numbers = list(range(b))
        sum_probability = map(lambda i: (a**i * e **(-a))/factorial(i), numbers)
        return 1 - sum(sum_probability)
    
a = 8
b = 12
s = prob_simpson(lamb=a, x=b)

print(s)