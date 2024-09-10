"""
Exercício: Sistema de Relatório Automatizado
Você foi encarregado de criar um sistema de relatórios automatizados usando a classe Template do Python.
 O objetivo é gerar relatórios personalizados para cada cliente de uma empresa. O sistema deve preencher 
 um template de relatório com as informações fornecidas de cada cliente.

Instruções:
Crie um template de relatório usando a classe Template da biblioteca string. O template deve conter 
 placeholders para as seguintes informações:

Nome do cliente
ID do cliente
Valor total da compra
Data da compra
Exemplo de template:

plaintext
Copiar código
Relatório de Compra:

Cliente: $nome_cliente
ID do Cliente: $id_cliente
Valor Total: R$ $valor_total
Data da Compra: $data_compra

Crie uma função chamada gerar_relatorio que recebe um dicionário com as informações do cliente (nome, ID, valor total, data) e o template, e retorne o relatório formatado.

Faça o tratamento de erros para garantir que todos os placeholders sejam preenchidos corretamente. Se alguma chave estiver faltando no dicionário, exiba uma mensagem de erro adequada.

Teste a função gerando relatórios para pelo menos 3 clientes diferentes
"""
from string import Template
from datetime import datetime
from locale import setlocale, LC_ALL, currency
from pathlib import Path

setlocale(LC_ALL, "")
RELATORIO = Path(__file__).home() / 'Desktop' / 'Autoconsciência' / 'Individuo' / 'relatorio.txt'

def converte_para_brl(numero:float):
    brl = 'R$' + currency(numero, symbol=False, grouping=True)
    return brl

class Relatorio:
    def __init__(self, id_funcionario:int, nome_cliente:str, data:str, valor_total:float) -> None:
        self.id_cliente = id_funcionario
        self.nome_cliente = nome_cliente
        self.data_comprar = datetime.strptime(data, "%d/%m/%Y").strftime("%d-%m-%Y")
        self.valor_total = converte_para_brl(valor_total)

    def gerar_relatorio(self):
        dados = self.__dict__
        with open(RELATORIO, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            template = Template(texto)
            return template.substitute(dados)
    

relatorio = Relatorio(
    1, 'João', '10/01/2024',
    2_000
)

relatorio_feito = relatorio.gerar_relatorio()
print(relatorio_feito)