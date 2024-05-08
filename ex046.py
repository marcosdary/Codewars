# Faça um programa que crie um vetor denominado A que armazene 8 números inteiros. O programa
#deve executar os seguintes passos:

# (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 3;

A = [1, 0, 5, -2, -5, 3]

# (b) Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] do
# vetor e mostre na tela esta soma;

print(f"Soma dos índices 1, 2, 6: {sum((A[0], A[1], A[5]))}") # Soma dos índices 1, 2, 6: 4

# (c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 239;

del A[4]
A.insert(4, 239)

# (d) Mostre na tela cada valor do vetor A, um em cada linha.

for i in A:
    print(f"índice {A.index(i)} valor {i}")