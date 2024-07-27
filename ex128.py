# números: [2,0, 2,0, 3,0, 4,0]
# regras: [ (a,b) => a + b, (a,b) => a - b ]
# resultado: 5,0

# Você obtém uma lista de quatro números.
# Existem duas regras. A primeira regra diz: Some os dois números a e b. A segunda regra diz: Subtraia b de a.

# As etapas para progredir:
# 1. Regra 1: Primeiro número + segundo número -> 2,0 + 2,0 = 4,0
# 2. Regra 2: resultado da etapa anterior - terceiro número -> 4,0 - 3,0 = 1,0
# 3. Regra 1: resultado da etapa anterior + quarto número -> 1,0 + 4,0 = 5,0

# reduce_by_rules([1.3, 2.0, 3.3])-> 3.3
# reduce_by_rules([2.9, 2.8, 2.7, 2.6, 2.5, 2.4]) -> 2.4

def reduce_by_rules(lst:list[float], rules) -> float:  
        
    pass
rules = [lambda a, b: a + b]
print(reduce_by_rules([2.0, 2.0, 3.0, 4.0], rules))