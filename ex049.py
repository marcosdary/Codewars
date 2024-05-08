# Faça um programa que permita ao usuário entrar com uma matriz de 3 x 3 números inteiros quaisquer.
# 
# Em seguida, gere um array unidimensional pela soma dos números de cada coluna da matriz e mostre na
# tela esse array. Por exemplo, a matriz:
# 
#           5 -8 10
#           1 2 15
#           25 10 7
# 
# Vai gerar um vetor, onde cada posição é a soma das dos valores de cada coluna dessa matriz. A primeira
# posição do vetor será a somatória de 5 + 1 + 25, e assim por diante.

matriz = []
vetor_colunas = [0, 0, 0]
i = 0
while i < 3:
    
    try:
        linha = []
        j = 0
    
        while j < 3:    
            n = int(input(f"Linha {i+1} Coluna {j+1}: "))
            linha.append(n)
            j += 1
    
        matriz.append(linha[:])
        i += 1 
        print('\n')    
    
    except ValueError as e:
        print(f"\n\tError: {e}\n")
        pass
    
for linha in matriz:
    
    for indice, elemento in enumerate(linha):
        
        vetor_colunas[indice] += elemento
        
print(vetor_colunas)
        

