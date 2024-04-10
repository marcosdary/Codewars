import random

matriz = []

for i in range(0, 15):
    coluna = []
    for j in range(0, 20):
        numero = random.randint(0, 99)
        coluna.append(numero)
    
    matriz.append(coluna[:])
    coluna.clear()
matriz_pares = []

for i in matriz:
    qtd_pares = len(list(filter(lambda j: j % 2 == 0, i)))
    soma = sum(filter(lambda j: j % 2 == 0, i))
    coluna = {"quantidade": qtd_pares, 'total': soma}
    matriz_pares.append(coluna.copy())
    coluna.clear()
    
matriz_impares = []
for i in matriz:
    qtd_impares = len(list(filter(lambda j: j % 2 != 0, i)))
    soma = sum(filter(lambda j: j % 2 != 0, i))
    coluna = {"quantidade": qtd_impares, 'total': soma}
    matriz_impares.append(coluna.copy())
    coluna.clear()
    
print(*matriz, sep="\n")
print()
print(*matriz_pares, sep='\n')
print()
print(*matriz_impares, sep='\n')