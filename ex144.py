import json
from functools import reduce
import os

caminho = os.path.join("C:\\Users\\Marcos e Matheus\\Documents\\GitHub\\Codewars\\gerenciador_produtos\\data_funcionario.json")

with open(caminho, 'r', encoding='utf-8') as file:
    datas = json.load(file)
    total_salario = reduce(lambda ac, s: ac + s['salario'], datas, 0)
    total_funcionario = len(datas)
    funcionario_maior_valor_vendido = max(datas, key=lambda f: f['valor_vendido'])
    total_vendas = reduce(lambda ac, s: ac + s['valor_vendido'], datas, 0)

    print(
        f'''
                        Dados

            Quantidade de funcionários: {total_funcionario}
            Valor total de pagamentos (R$): {total_salario:,.0f}
            Média salarial (R$): {total_salario/total_funcionario:,.2f}
            Receita (R$): {total_vendas:,.2f}
        '''
    )
    print(
        f'''
            Funcionário com maior receita
            cargo: {funcionario_maior_valor_vendido['cargo']}
            salário (R$): {funcionario_maior_valor_vendido['salario']:,.2f}
            receita requerida (R$): {funcionario_maior_valor_vendido['valor_vendido']:,.2f} 
        '''
    )

          