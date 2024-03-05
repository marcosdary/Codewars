
from math import pi, sqrt 
def decorator_function(func):
    
    def inner_function(*args, **kwargs):
        if validation_values(*args):
            return 'Valor inválido'
        return func(*args, **kwargs)
    
    return inner_function

@decorator_function
def ellipse(a, b):
    
    
    area = pi * (a * b)
    perimeter = pi * (3/2*(a+b) - sqrt(a*b))
    return f"Area: {area:.1f}, perimeter: {perimeter:.1f}"

def validation_values(*args):
    for arg in args:
        if arg < 0:
            return True

output = ellipse(12, 78)
print(output)

