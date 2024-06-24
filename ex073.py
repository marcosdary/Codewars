# - A unidade de bônus é 1K ($1000), e cada equipe recebe pelo menos 1k.
# - O processo de pagamento do bônus não é público.
#
# - Uma equipe pode saber o valor do bônus de sua equipe adjacente, se o
# a pontuação da equipe adjacente é menor que ela mesma.
#
# - Se uma equipe descobrir que seu bônus não é maior que o da equipe adjacente cuja
# a pontuação for menor que ela mesma, a equipe não ficará satisfeita
class Bonus:
    def __init__(self, group:list) -> None:
        self.group = group

    def bonus(self):
        t = len(self.group)
        gruopbonus = [1]*t
        
        for j in range(1, t):
            
            if self.group[j-1] < self.group[j]:
                value = gruopbonus[j-1] + 1 
                gruopbonus[j] = value
        print(self.group)
        print(gruopbonus)
        for i in range(t-2, -1, -1):
            print(f'Primeiro número {self.group[i]} observa o segundo número {self.group[i+1]}')
            if self.group[i+1] < self.group[i]:
                value = max(gruopbonus[i], gruopbonus[i+1] + 1)
                gruopbonus[i] = value
        print(gruopbonus)
        return sum(gruopbonus)
    
def minimum_bonus(scores:list):
    b = Bonus(scores)
    return b.bonus()


# pontuação da equipe1 = 10
# pontuação do time2 = 20
# pontuação do time3 = 30

# team1 pode ganhar 1K, a equipe ficou satisfeita
# porque não sabia nada sobre as outras equipes.

# team2 pode saber o valor do bônus da equipe1,
# Então o time2 consegue pelo menos 2K para ficar satisfeito

# team3 pode saber o valor do bônus do team2,
# Então o time3 consegue pelo menos 3K para ficar satisfeito

# 1 + 2 + 3 = 6

# Para scores = [10,20,20,30], a saída deve ser 6.

# O possível valor do bônus de cada equipe pode ser:[1,2,1,2]

# For scores = [20,30,10,30,40,10,20,30,40,30], the output should be 20.

# The possible bonus amount of each team can be:[1,2,1,2,3,1,2,3,4,1]
# Saída
scores = [20, 30, 40, 30, 20, 10]
print(minimum_bonus(scores))
