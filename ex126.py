'''
Você está jogando euchre e quer saber a nova pontuação após terminar uma mão. 
Há dois times e cada mão consiste em 5 vazas. O time que ganhar a maioria das vazas
ganhará pontos, mas o número de pontos varia. Para determinar o número de pontos,
você deve saber qual time chamou trunfo, quantas vazas cada time ganhou e se 
alguém foi sozinho. A pontuação é a seguinte:

Para a equipe que escolheu Trump:
se eles ganharem 2 ou menos vazas -> o outro time ganha 2 pontos
se ganharem 3 ou 4 vazas -> 1 ponto
se não forem sozinhos e ganharem 5 vazas -> 2 pontos
se eles forem sozinhos e ganharem 5 vazas -> 4 pontos

Somente o time que disse trunfo pode jogar sozinho e você notará 
que seus pontos só aumentam se você vencer todas as 5 vazas.

Seu trabalho é criar um método para calcular a nova pontuação. 
Ao ler os argumentos, o time 1 é representado por 1 e o time 2 é 
representado por 2. Todas as pontuações serão armazenadas com esta ordem: { team1, team2 }

update_score([0, 0], 1, False, [1, 1, 1, 1, 1]), [2, 0] -> "A pontuação é 0 a 0. O time 1 chama 
o trunfo (não vai sozinho) e ganha 5 vazas"
update_score([2, 0], 2, False, [2, 1, 2, 2, 2]) -> [2, 1]
update_score([2, 1], 1, False, [1, 2, 2, 1, 1]) -> [3, 1]
update_score([3, 1], 2, True, [2, 2, 2, 2, 2]) -> [3, 5]
update_score([3, 5], 1, True, [1, 2, 2, 2, 1]) -> [3, 7]
update_score([0, 0], 1, False, [1, 1, 1, 1, 1]) -> [2, 0]
'''
from collections import Counter

def update_score(pontuacao_atual:list[int], quem_time_chamou:int, sozinho:bool, partidas:list[int]) -> list[int]:
    pontuacao_nova = {1: pontuacao_atual[0], 2: pontuacao_atual[1]}
    quantidade = Counter(partidas)
    time = max(quantidade.items(), key=lambda k: k[1])
    
    if quem_time_chamou == time[0] and sozinho and time[1] == 5:
        pontuacao = 4

    elif not sozinho and time[0] == quem_time_chamou and time[1] == 5:
        pontuacao = 2

    elif time[0] == quem_time_chamou and time[1] in [3, 4]:
        pontuacao = 1

    else:
        pontuacao_rival = 2
    print(time, pontuacao)
    
    if quem_time_chamou == time[0]:
        pontuacao_nova[time[0]] += pontuacao
        return list(pontuacao_nova.values())
    
    pontuacao_nova[time[0]] += pontuacao_rival
    return list(pontuacao_nova.values())
    
    

print(update_score([2, 1], 1, False, [1, 2, 2, 1, 1]))