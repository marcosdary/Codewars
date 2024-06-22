# Número Catalão
# (2n)! / ((n + 1)! * n!)
import math
from fractions import Fraction
def nth_catalan_number(n):
    
    num_catalan = Fraction(math.factorial(2*n)) / (Fraction(math.factorial(n+1)) * Fraction(math.factorial(n)))
    return int(num_catalan)

print(nth_catalan_number(71))