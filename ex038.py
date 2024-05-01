# Projeto: Sistema de Gerenciamento de Funcionários em uma Empresa

# Classes Base:
# Crie uma classe Pessoa com os atributos nome, idade e cpf.
# Crie uma classe Endereco com os atributos rua, numero, cidade e estado.

# Subclasses:
# Crie uma subclasse Funcionario que herda da classe Pessoa e adiciona os atributos cargo e salario.
# Crie uma subclasse Gerente que herda da classe Funcionario e adiciona o atributo departamento.
# Funcionalidades:
# Adicione métodos nas classes para exibir informações dos objetos.
# Implemente um método na classe Funcionario para calcular o salário líquido após descontos.
# Crie objetos das subclasses e teste os métodos implementados.

def isCpf(cpf:str):
    cpf = cpf.replace(".", '').replace('-', '')
    if cpf == 11:
        return False
    
    digito_verificador = 0
    for i in range(len(cpf[:9])):
        d = 10 - i
        if d > 1:
            digito_verificador += int(cpf[i]) * d
            
    digito_verificador = (digito_verificador * 10) % 11
    if digito_verificador == 10 or digito_verificador == 11:
        digito_verificador = 0
    
    if digito_verificador != int(cpf[9]):
        return False
    
    digito_verificador = 0
    for i in range(len(cpf[:10])):
        d = 11 - i
        if d > 1:
            digito_verificador += int(cpf[i]) * d
            
    digito_verificador = (digito_verificador * 10) % 11
    if digito_verificador == 10 or digito_verificador == 11:
        digito_verificador = 0
    if digito_verificador != int(cpf[10]):
        return False
    
    return True


class Pessoa:
    def __init__(self, nome:str, idade:int,) -> None:
        self.nome = nome
        self.idade = idade
        self._cpf = None
    
    @property    
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf_user):
        if isCpf(cpf_user):
            self._cpf = cpf_user
        else:
            print("\tCPF inválido")

class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.__cargo = None
        self._salario = None
    
    
    @property    
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo_user:str):
        self.__cargo = cargo_user
            
    @property    
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario_user:float):
        if salario_user > 0:
            self._salario = salario_user
            
    def salario_liquido(self, descontos:float):
        sl = 1 - descontos
        return self._salario * sl
    
    def __str__(self) -> str:
        return f'Funcionário: {self.nome}\nSalário Bruto: {self.salario}\nCPF: {self.cpf}\nCargo: {self.cargo}'
    
class Gerente(Funcionario):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.__departamento = None
        
    @property    
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento_user:str):
        self.__departamento = departamento_user
        
    def __str__(self) -> str:
        return f'Gerente: {self.nome}\nSalário Bruto: {self.salario}\nCPF: {self.cpf}\nDepartamento: {self.departamento}'
        
        
class Endereco:
    def __init__(self, rua:str, numero:int, cidade:str = 'São Paulo', estado:str = 'São Paulo') -> None:
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        
        
# Teste
gerente = Gerente('Caio', 20)
gerente.cpf = '169.169.000-75'
gerente.salario = 7800.45
gerente.departamento = 'Recursos Humanos'
gerente.salario_liquido(0.084)


funcionario = Funcionario('Davi', 34)
funcionario.salario = 1789.45
funcionario.cargo = 'Desernvolvedor'
funcionario.cpf = '169.169.000-75'
