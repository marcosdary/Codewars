from pathlib import Path
from csv import writer, DictWriter

DESKTOP = Path().home() / 'Desktop'
LOUCURA = DESKTOP / 'Loucura' / 'Sentimentos.csv'

sentimentos = [
    {'Emoção': 'Raiva', 'Estado': "Médio"},
    {'Emoção': 'Ansiedade', 'Estado': "Alto"},
    {'Emoção': 'Frustação', 'Estado': 'Baixo'},
    {'Emoção': 'Loucura', 'Estado': 'Baixo'},
    {'Emoção': 'Ressentimento', 'Estado': 'Alto'}
]

with open(LOUCURA, 'w', encoding='utf-8') as file:
    nomes_campos = sentimentos[0].keys()
    
    escrita = DictWriter(
        file,
        fieldnames=nomes_campos # Adicionar o nomes dos campos que serão pegos pela a variável "escrita"
    )
    escrita.writeheader() # Escreve o titulo de cada campo, por exemplo, nesse csv, tem "Emoção" e "Estado"
                          # Pode esse motivo pode ser opicional
    
    for sentimento in sentimentos:
        escrita.writerow(sentimento) # Escreve os dados para o csv
    
with open(LOUCURA, 'w', encoding='utf-8') as file:
    nomes_campos = sentimentos[0].keys()
    
    escrita = writer(file)
    escrita.writerow(nomes_campos) # Adicionar o nomes do campos
    for sentimento in sentimentos:
        escrita.writerow(sentimento.values()) # Escreve os dados dos campos
        
