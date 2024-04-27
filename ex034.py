class Endereco:
    def __init__(self, rua, numero, cidade, estado) -> None:
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self._endereco = None
        
    def endereco(self, rua, numero, cidade, estado):
        self.endereco = Endereco(rua, numero, cidade, estado)
        
class Empresa:
    def __init__(self, nome, cnpj) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self._funcionarios = []
    
    def add_funcionario(self, nome):
        self._funcionarios.append(nome)
        
    @property
    def funcionario(self):
        return self._funcionarios
    
# Criando alguns endereços
rua1, numero1, cidade1, estado1 = "Rua A", 123, "Cidade A", "Estado A"
rua2, numero2, cidade2, estado2 ="Rua B", 456, "Cidade B", "Estado B"

# Criando algumas pessoas
pessoa1 = Pessoa("João", 30)
pessoa1.endereco(rua1, numero1, cidade1, estado1)
pessoa2 = Pessoa("Maria", 25)
pessoa2.endereco(rua2, numero2, cidade2, estado2)
# Criando uma empresa
empresa = Empresa("Minha Empresa", "123456789")

# Contratando funcionários
empresa.add_funcionario(pessoa1)
empresa.add_funcionario(pessoa2)

# Verificando os funcionários da empresa
for funcionario in empresa.funcionario:
    print(f"Funcionário: {funcionario.nome}, Endereço: {funcionario.endereco.rua}, {funcionario.endereco.numero}, {funcionario.endereco.cidade}, {funcionario.endereco.estado}")