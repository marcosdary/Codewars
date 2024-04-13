"""
1. Faça um programa que leia uma matriz A que armazene 12 nomes de
pessoas informados pelo usuário. O algoritmo deverá procurar na matriz
se existe um determinado nome que foi informado pelo usuário. Caso
exista, exibir uma mensagem avisando que encontrou e em qual posição
da matriz. Caso não, exibir uma mensagem de que o nome não foi
encontrado.
2. Crie uma matriz quadrada e a inicialize de forma que seja atribuído o valor
2 quando os índices forem iguais e -3 quando os índices forem diferentes.
Calcule e imprima na tela apenas o somatório da diagonal principal.
3. Escreva um programa que tenha uma matriz de 12 elementos quaisquer
informados pelo usuário e imprima quantos elementos são pares e
quantos são ímpares, bem como a soma total de cada um."""

"""
Desenvolvi um programa em Python que, por meio da entrada do usuário, 
constrói uma matriz com 12 elementos diferentes. Em seguida, 
o programa deve realizar uma análise avançada, 
determinando a quantidade de elementos pares e ímpares na matriz, 
além de calcular a soma total dos elementos pares e ímpares separadamente"""
        

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