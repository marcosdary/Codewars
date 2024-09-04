# Carregando dados para um arquivo csv 
from pathlib import Path
from csv import DictReader, DictWriter
from datetime import datetime


DESKTOP = Path().home() / 'Desktop'
DIR_TENDENCIAS_MERCADO = DESKTOP / 'Tendencias de mercado' 
FILE_VENDAS = DIR_TENDENCIAS_MERCADO / 'vendas.csv'
FILE_RELATORIO = DIR_TENDENCIAS_MERCADO 

with open(FILE_VENDAS, 'r', encoding='utf-8') as file:
    vendas = [campo for campo in DictReader(file)]

CAMPOS = [
   'ID da Venda', 'Data', 'Produto', 'Quantidade', 
   'Preço Unitário', 'Total da Venda', 'Categoria do Produto'
] 

# 1) Exibir Resumo de Vendas: Mostrar um resumo das vendas, incluindo total de vendas, número de transações e média de vendas por transação.

resumo_vendas = {'total_vendas': 0, 'total_transacoes': 0, 'media_transacao': None}

for venda in vendas:
    resumo_vendas['total_vendas'] += float(venda['Total da Venda'])
    resumo_vendas['total_transacoes'] += 1

resumo_vendas['media_transacao'] = resumo_vendas['total_vendas'] / resumo_vendas['total_transacoes']

# 2) Permitir a filtragem dos registros de vendas por um intervalo de datas específico.
data_inicial = datetime.strptime('2024-09-01', '%Y-%M-%d')
data_final = datetime.strptime('2024-09-04', '%Y-%M-%d')
vendas_apartir_do_condicao_atendida = []

for venda in vendas:
   
    if data_inicial <= datetime.strptime(venda['Data'], '%Y-%M-%d') < data_final:
        vendas_apartir_do_condicao_atendida.append(venda)
 
# 3) Inserir um novo registro de venda no arquivo CSV.

dados_vendas = [
    ['2024-01-05',	'Smartphone Galaxy S23', '2', 5000.00, 10000.00,'Eletrônicos'], 
    ['2024-01-10',	'Notebook Dell XPS 13',	'1', 8000.00, 8000.00,	'Informática'],
    ['2024-01-15',	'Fone de Ouvido Airpods', '4', 1500.00,	6000.00, 'Áudio']
]
lista_dicionario = []
i = 21
for dado_venda in dados_vendas:
    dicionario = {}
    dicionario["ID da Venda"] = f'{i}'
    for index, dado in enumerate(dado_venda):
        dicionario[CAMPOS[index+1]] = dado
      
    vendas.append(dicionario)
    i += 1

# 4) Atualizar um registro de venda existente com base em um identificador único, como o ID da venda.
id_venda_atualizar = '1'
for venda in vendas:
    id_venda = list(venda.items())[0]
    if id_venda[1] == id_venda_atualizar:
        venda['Preço Unitário'] = str(2700)
        venda['Total da Venda'] = str(2700 * int(venda['Quantidade']))
 

# 5) Remover um registro de venda do arquivo CSV.
id_venda_remover = '3'
for index, venda in enumerate(vendas):
    id_venda = list(venda.items())[0]
    if id_venda[1] == id_venda_remover:
        vendas.pop(index)
        break

# 6) Criar relatórios de vendas em formato CSV com base em filtros aplicados, como vendas por produto, por período, ou por categoria

# Filtro por produto
data_inicial = datetime.strptime('2024-09-01', '%Y-%M-%d')
data_final = datetime.strptime('2024-09-04', '%Y-%M-%d')
vendas_de_projetor = []
vendas_de_informatica = []
vendas_por_periodo = []

for venda in vendas:
   
    if venda['Produto'] == 'Projetor':
        vendas_de_projetor.append(venda)
    if venda['Categoria do Produto'] == 'Informática':
        vendas_de_informatica.append(venda)
    if data_inicial <= datetime.strptime(venda['Data'], '%Y-%M-%d') < data_final:
        vendas_por_periodo.append(venda)


def escrever_csv(nome, dados:list[dict], caminho=FILE_RELATORIO):
    with open(caminho / nome, 'w', encoding='utf-8') as file:
        escrever = DictWriter(file, fieldnames=CAMPOS)
        escrever.writeheader()
        for dado in dados:
            escrever.writerow(dado)
        return

escrever_csv('vendas_de_projetor.csv', vendas_de_projetor)
escrever_csv('vendas_de_informatica.csv', vendas_de_informatica)
escrever_csv('vendas_por_periodo.csv', vendas_por_periodo)