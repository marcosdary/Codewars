from functools import partial, reduce
from itertools import groupby

nomes = (
    "Ana", "Pedro", "Maria", "João", "Sofia", "Carlos", "Luísa", "André", "Laura", "Tiago"
    )
idades = (
    25, 32, 19, 45, 28, 36, 22, 30, 41, 20
    )
sexo = (
    "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", "Masculino"
    )

# total de pessoas: em que abrigar todas as pessoas da lista anteriores, tipo 
# uma junção
lista_pessoas = [
    {'nome': nome, 'idade': idade, 'sexo': sexo}
    for nome, idade, sexo in zip(nomes, idades, sexo)
]

# pessoas que possuem o idade menor que a média das idades
media_idades = sum(idades)/len(idades)
lista_pessoas_com_idades_menores_que_media = list(filter(lambda pessoa: pessoa['idade'] < media_idades, lista_pessoas))

# quantidade de pessoas com sexo masculino
total_pessoas_masculinas = reduce(
    lambda ac, p: ac + 1 if p['sexo'] == 'Masculino' else ac, lista_pessoas, 0
) # Aqui foi utlizado a função lambda, com duas condicionais. Uma para soma 1 ao ac caso o p['sexo'] seja 'Masculino', se não ac continuar
  # igual ao anterior
                                                                                                             

# criar um ordem com a iterator groupby
sexo_agrupados = sorted(lista_pessoas, key= lambda i: i['sexo'])
ordenar_por_sexo = groupby(sexo_agrupados, key = lambda i: i['sexo'])

for chave, valores in ordenar_por_sexo:
    print(chave)
    for valor in valores:
        print(f'{valor["nome"]:<12}{valor["idade"]}')
    print()
