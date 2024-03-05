# Inicializar uma lista para armazenar os pares de números que somam 20
from math import sqrt
pares_20 = []
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
# Loop para gerar pares de números únicos
for i in range(1, 27):
    # Verificar se a soma de i e (20 - i) é igual a 20
    if (26 - i) == i:
        pares_20.append((i, i))
    elif (26 - i) > i:
        pares_20.append((i, 26 - i))

# Imprimir os pares que somam 20
print("Pares que somam 20:")
for par in pares_20:
    if is_prime(par[0]) and is_prime(par[1]):
        print(par)
    