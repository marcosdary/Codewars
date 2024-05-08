# Faça um programa que leia um conjunto de números reais, armazenando-os em vetor e depois calcule
# o quadrado de cada um destes valores desse primeiro vetor e os armazene em outro vetor em posições
# inversas. O conteúdo dos dois vetores deve ser exibido.

def adicionar_numero(a, vetor = None):
    
    if vetor is None:
        vetor = []
    vetor.append(a)
    
    return vetor
try:
    indice = int(input("Máximo índice: "))

    numeros_reais = adicionar_numero(0)
    for i in range(1, indice+1):    

        adicionar_numero(i/2, numeros_reais)
        
    numeros_reais_inverso = adicionar_numero(pow(numeros_reais[-1], 2))
    for index in range(len(numeros_reais)-2, -1, -1):
        
        adicionar_numero(pow(numeros_reais[index], 2), numeros_reais_inverso)
        
except ValueError as e:
    print(f"\n\tError: {e}\n")

