from pathlib import Path
from csv import reader, DictReader

DESKTOP = Path().home() / 'Desktop'
LOUCURA = DESKTOP / 'Loucura' / 'Sentimentos.csv'
print(LOUCURA.exists())

with open(LOUCURA, 'r', encoding='utf-8') as file:
    dados_csv = DictReader(file)
    # nome_campo_1, nome_campo_2 = next(dados_csv)
    # print(f'{nome_campo_1:<20} {nome_campo_2:<4}')
    for dado in dados_csv:
        # campo_1 , campo_2 = dado
        # print(f'{campo_1:<20} {campo_2:<4}')
        print(f'{dado}')
