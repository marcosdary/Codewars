from string import Template
from datetime import datetime
from locale import setlocale, LC_ALL, currency
from pathlib import Path

setlocale(LC_ALL, "")
RELATORIO = Path(__file__).home() / 'Desktop' / 'Autoconsciência' / 'Individuo' / 'relatorio.txt'

def converte_para_brl(numero:float):
    brl = 'R$ ' + currency(numero, symbol=False, grouping=True)
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