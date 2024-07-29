from datetime import datetime, timedelta
from dataclasses import dataclass

@dataclass
class Emprestimo:
    valor_emprestimo: float
    quantidade_de_tempo_emprestimo: int
    data_equisicao_emprestimo: str
    quantidade_de_parcelas: int

    @property
    def data_inicio_pagamento_emprestimo(self):
        return datetime.strptime(self.data_equisicao_emprestimo, '%d/%m/%Y') + timedelta(days=self.quantidade_de_tempo_emprestimo*365)
    
    def parcelas(self):
        lista_parcela_data = [
            {
                'parcela': self.valor_emprestimo / self.quantidade_de_parcelas,
                'data': datetime.strptime(self.data_equisicao_emprestimo, '%d/%m/%Y') + timedelta(days=i * 30)
            }
            for i in range(1, (self.quantidade_de_tempo_emprestimo * 12)+1)
        ]
        return lista_parcela_data

    

valor_emprestimo = 1_000_000
data_aquisicao_emprestimo = '20/12/2020'
tempo_pagamento_emprestimo = 5
quantidade_de_parcela_emprestimo = 60

emprestimo = Emprestimo(
    valor_emprestimo=valor_emprestimo,
    data_equisicao_emprestimo=data_aquisicao_emprestimo,
    quantidade_de_tempo_emprestimo=tempo_pagamento_emprestimo,
    quantidade_de_parcelas=quantidade_de_parcela_emprestimo
)

print(f'Previsão de pagamento da última parcela: 20-{emprestimo.data_inicio_pagamento_emprestimo.strftime("%m-%Y")}\n')
for i, parcela in enumerate(emprestimo.parcelas()):
    valor_parcela = parcela['parcela']
    print(f'Data: 20-{datetime.strftime(parcela['data'], '%m-%Y')} - {i+1}° Parcela(R$): {parcela['parcela']:,.2f}')
print(f'\nVocê pegou R${valor_emprestimo:,} para pagar em 5 anos ({quantidade_de_parcela_emprestimo} meses) em parcela de R${valor_parcela:,.2f}')

