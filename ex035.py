class Produto:
    def __init__(self, nome:str, codigo:int) -> None:
        self.nome = nome
        self.codigo = codigo
        self._preco = None
        self.__qtd_estoque = 0
        self.__qtd_sai_estoque = 0
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor:float):
        
        if valor > 0:
            self._preco = valor
            
        else:
            print(f'Preço: {False}')
    
    @property
    def qtd_estoque(self):
        return self.__qtd_estoque
    
    @property
    def qtd_sai_estoque(self):
        return self.__qtd_sai_estoque
    
    @qtd_estoque.setter
    def qtd_estoque(self, valor:int):
        
        if valor > 0:
            self.__qtd_estoque += valor
            
        else:
            print(f'Estoque: {False}')
            
    def diminuir_estoque(self, valor:int):
        
        if valor > 0 and self.__qtd_estoque >= valor:
            self.__qtd_sai_estoque += valor
            
        else:
            print(f'Diminuir estoque: {False}')
    
class Fornecedor:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self._cnpj = None
        self._produtos = []
    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, valor:int):
        
        if valor > 0:
            self._cnpj = valor
            
        else:
            print(f'CNPJ: {False}')
    
    @property
    def produtos(self):
        return self._produtos
    
   
    def inserir_produto(self, valor):
        self._produtos.append(valor)
        
    def __str__(self) -> str:
        print(f'Empresa: {self.nome}\nCNPJ: {self.cnpj}\n')
        
        for produto in self._produtos:
            print(f"Produto: {produto.nome}\nCódigo: {produto.codigo}\nEntrada: {produto.qtd_estoque}\nSaída: {produto.qtd_sai_estoque}\n")
            
        return ''
        
          
class Pedido:
    def __init__(self, cliente:str, num_pedido:int, data_pedido:str) -> None:
        self.cliente = cliente
        self.num_pedido = num_pedido
        self.data_pedido = data_pedido
        self._status_pedido = None
        self._lista_itens = []
        
        
    
    @property
    def status_pedido(self):
        return self._status_pedido
    
    @status_pedido.setter
    def status_pedido(self, valor:str):
        
        if valor.isalpha() and valor in ('aberto', 'fechado', 'entregue'):
            self._status_pedido = valor
            
        else:
            print(f'Status resposta: {False}')
    
    @property
    def lista_itens(self):
        return self._lista_itens
    
    def inserir_pedido(self, produto, quant, fornecedor):
        if produto in fornecedor.produtos:
            fornecedor.produtos[fornecedor.produtos.index(produto)].diminuir_estoque(quant)
            pedido_dict = {'produto': produto, 'quantidade': quant, 'fornecedor': fornecedor}
            self._lista_itens.append(pedido_dict)
        else:
            print(f'Fornecedor: {fornecedor.nome} não têm este produto')
    
    def valor_total_pedido(self):
        v = 0
        for item in self._lista_itens:
            print(f'\tProduto: {item['produto'].nome}\n\tPreço: {item['produto'].preco}\n\tQuantidade: {item['quantidade']}\n\t\tValor: {round(item['produto'].preco * item['quantidade'], 3)}')
            v += item['produto'].preco * item['quantidade']
        print(f"Valor total: {v:.2f}R$")
        
    def __str__(self) -> str:
        print(f'\tCliente: {self.cliente}\n\tData do pedido: {self.data_pedido}\n\tCódigo do pedido: {self.num_pedido}\n')
        
        for item in self._lista_itens:
            print(f"Produto: {item['produto'].nome}\nQuantidade: {item['quantidade']}\nFornecedor: {item['fornecedor'].nome}\n")
            
        return ''
        
        
# Produto
produto_a = Produto('Calça', 4789)
produto_a.preco = 54.7
produto_a.qtd_estoque = 1000

produto_b = Produto('Jaqueta', 7894)
produto_b.preco = 128.45
produto_b.qtd_estoque = 200

produto_c = Produto('Blusa', 1236)
produto_c.preco = 78.45
produto_c.qtd_estoque = 20

produto_d = Produto('Suéter', 9000)
produto_d.preco = 136.45
produto_d.qtd_estoque = 1200

# Fornecedor
fornecedor_a = Fornecedor('Riachuelo')
fornecedor_a.cnpj = 7894612
fornecedor_a.inserir_produto(produto_a)
fornecedor_a.inserir_produto(produto_b)

fornecedor_b = Fornecedor('C&A')
fornecedor_b.cnpj = 4569784
fornecedor_b.inserir_produto(produto_c)
fornecedor_b.inserir_produto(produto_d)

# Pedido
pedido_a = Pedido('Mark', 457912, '12/01/2021')
pedido_a.status_pedido = 'aberto'
pedido_a.inserir_pedido(produto_a, 3, fornecedor_a)
pedido_a.inserir_pedido(produto_d, 10, fornecedor_b)

pedido_b = Pedido('Rose', 458912, '12/02/2021')
pedido_b.status_pedido = 'aberto'
pedido_b.inserir_pedido(produto_b, 3, fornecedor_a)
pedido_b.inserir_pedido(produto_c, 19, fornecedor_b)

