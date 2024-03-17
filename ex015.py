# Requisitos
# Calcule a soma do quadrado de cada dígito individual.
# Se a soma for igual a 1, então o número é happy
# Um número é considerado unhappyquando o mesmo número ocorre várias 
#   vezes em uma sequência porque isso significa que há um loop e nunca chegará a 1

# Por exemplo, o número 7 é um número “feliz”:
#   7² = 49 --> 4² + 9² = 97 --> 9² + 7² = 130 --> 1² + 3² + 0² = 10 --> 1² + 0² = 1
# o número 6 não é um número feliz porque a sequência gerada é a seguinte:
# 6, 36, 45, 41, 17, 50, 25, 29, 85, '89' , 145, 42, 20, 4, 16, 37, 58, '89'#

from itertools import combinations_with_replacement, permutations
from functools import reduce
from bisect import bisect


# Nessa função, será formatada a própria execução do problema
def perf_happy(n):
    return HAPPY_NUMBER[:bisect(HAPPY_NUMBER, n)]

# Pré-cálculo

def precalculate_happy(limit):
    
    sums_happy = [map(str, seq) for seq in combinations_with_replacement(range(10), limit) if pow_ndividual_digit(reduce(lambda ac, x: ac + str(x), seq, ''))]

    return sorted({int(''.join(x)) for seq in sums_happy for x in permutations(seq)})
 
# Aqui irá pegar o resultado da número, para retorná-lo ao quadrado.

def pow_ndividual_digit(digit):
    for _ in range(7):
        
        digit = sum(int(x)**2 for x in str(digit))
        if digit == 1:
            return True
    return False
HAPPY_NUMBER = precalculate_happy(7)


test_1 = 100 # [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
test_2 = 10_000_000
check_test_happy = perf_happy(test_2)
print(check_test_happy)
            