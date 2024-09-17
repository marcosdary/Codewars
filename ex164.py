class Pedido:
    def __init__(self, produto: str, valor: float, quantidade: int) -> None:
        self.produto = produto
        self.valor = valor
        self.quantidade = quantidade

    def __repr__(self) -> str:
        return f"{type(self).__name__}(produto={self.produto}, valor={self.valor}, quantidade={self.quantidade})"


class CarrinhoDeCompras:  # Composição
    def __init__(self) -> None:
        self.pedidos = []

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)

    def __del__(self):
        # Quando o carrinho for destruído, todos os pedidos também serão
        print("Carrinho destruído, todos os pedidos serão removidos.")
        self.pedidos.clear()

    def __repr__(self) -> str:
        return f"CarrinhoDeCompras(pedidos={self.pedidos})"


class Endereço:  # Agregação
    def __init__(self, rua: str, cidade: str, cep: str) -> None:
        self.rua = rua
        self.cidade = cidade
        self.cep = cep

    def __repr__(self) -> str:
        return f"Endereço(rua={self.rua}, cidade={self.cidade}, cep={self.cep})"


class Pessoa:
    def __init__(self, nome: str, email: str, endereco: Endereço) -> None:
        self.nome = nome
        self.email = email
        self.endereco = endereco  # Agregação: Pessoa tem um endereço, mas o endereço pode existir por si só  


    def __repr__(self) -> str:
        return f"Pessoa(nome={self.nome}, email={self.email}, endereco={self.endereco})"


class Cliente(Pessoa):  # Herança
    def __init__(self, nome: str, email: str, endereco: Endereço, cliente_id: str) -> None:
        super().__init__(nome, email, endereco)
        self.cliente_id = cliente_id
        self.carinho_compras = CarrinhoDeCompras()

    def realizar_pedido(self, pedido: Pedido) -> bool:
        self.carinho_compras.adicionar_pedido(pedido=pedido)
        return True

    def __repr__(self) -> str:
        return f"Cliente(nome={self.nome}, cliente_id={self.cliente_id})"


class Funcionario(Pessoa):  # Herança
    def __init__(self, nome: str, email: str, endereco: Endereço, matricula: str) -> None:
        super().__init__(nome, email, endereco)
        self.matricula = matricula

    def __repr__(self) -> str:
        return f"Funcionario(nome={self.nome}, matricula={self.matricula})"


endereco = Endereço("São José", "São Paulo", "79046-78")
cliente = Cliente(cliente_id='1', nome="Carlos", email="carlos@example.com", endereco=endereco)
pedido_1 = Pedido("Amendoim", 5.6, 2)
pedido_2 = Pedido("Arroz", 2.9, 2)
pedido_3 = Pedido("Feijão", 4.6, 10) 
cliente.realizar_pedido(pedido_1)
cliente.realizar_pedido(pedido_2)
cliente.realizar_pedido(pedido_3)


for pedido in cliente.carinho_compras.pedidos:
    print(pedido)

print("")
print(cliente.endereco)
