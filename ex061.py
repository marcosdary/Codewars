# Faça um programa para cadastrar 100 produtos de uma loja com os
# seguintes dados: código do produto, quantidade mínima em estoque,
# quantidade atual em estoque e o preço. O programa deve:

# a) mostrar todos os dados dos produtos que contenham o estoque atual
# menor que o estoque mínimo para efetuar compra;

# b) calcular o valor total dos produtos em estoque.
import functools
produtos = []

produto = {}
i = 0
while i < 100:
    try:
        codigo_produto = str(input("Código do produto: "))
        quantidade_minima = int(input("Quantidade mínima: "))
        quantidade_atual = int(input("Quantidade atual: "))
        preco = float(input("Preço: "))
        print("")
        if quantidade_minima < 0 and quantidade_atual < 0 and preco < 0:
            raise ValueError("Um dos valores são negativos")
    except ValueError as err:
        print(f"\n\tError: {err}")
    
    else:
        produto['codigo'] = codigo_produto
        produto['quant_minima'] = quantidade_minima
        produto['quant_atual'] = quantidade_atual
        produto['preco'] = preco
        produtos.append(produto.copy())  
        i += 1

menor_quantidade = list(filter(lambda i: i['quant_minima'] > i['quant_atual'], produtos))
soma_total = functools.reduce(lambda ac, pr: ac + pr['preco']*pr['quant_atual'], produtos, 0)

print(f"Dados dos produtos que contenham o estoque atual menor que o estoque mínimo para efetuar compra")
print(*menor_quantidade, sep='\n')

print()
print(f'Valor total dos produtos em estoque: {round(soma_total, 2)}')

    
    