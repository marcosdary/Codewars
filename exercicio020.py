from abc import ABC, abstractmethod

class Agencia:
    def __init__(self, numero_agencia:int, cidade:str, endereco:str) -> None:
        self.numero_agencia = numero_agencia
        self.cidade = cidade
        self.endereco = endereco

    def __repr__(self) -> str:
        return f'{type(self).__name__}(numero_agencia={self.numero_agencia},cidade={self.cidade},endereco={self.endereco})'
    
    def __str__(self) -> str:
        return f'Número da agência: {self.numero_agencia}\nCidade: {self.cidade}\nEndereço: {self.endereco}'

class ContaBancaria(ABC):
    def __init__(self, numero_conta:int, saldo:float) -> None:
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor:float):
        pass

    def depositar(self, valor:float):
        self.saldo += valor
        return True

class Poupanca(ContaBancaria):
    def __init__(self, numero_conta:int, saldo:float) -> None:
        super().__init__(numero_conta, saldo)

    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
    
    def rendimento(self, taxa:float, tempo:int):
        return self.saldo + self.saldo * taxa * tempo
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}(numero_conta={self.numero_conta},saldo={self.saldo})'
    
    def __str__(self) -> str:
        return f'Conta: Poupança\nNúmero da conta: {self.numero_conta}\nSaldo: {self.saldo}'

class Corrente(ContaBancaria):
    def __init__(self, numero_conta: int, saldo: float) -> None:
        super().__init__(numero_conta, saldo)
        self.__limite = 0

    @property
    def limte(self):
        return self.__limite
    
    @limte.setter
    def limite(self, valor:float):
        if valor > 0:
            self.__limite = valor
            return True
        return False

    def sacar(self, valor: float):
        if self.limite <= valor:
            self.saldo -= valor
            return valor
        return False

    def transferir(self, conta_destino:ContaBancaria, valor:float):
        if valor <= self.limite:
            self.saldo -= valor
            conta_destino.saldo += valor
            return True
        return False
    
    def __str__(self) -> str:
        return f'Conta: Corrente\nNúmero da conta: {self.numero_conta}\nSaldo: {self.saldo}\nLimite: {self.__limite}'

class Pessoa(ABC):
    def __init__(self, nome:str, endereco:str) -> None:
        self.nome = nome
        self.endereco = endereco

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Funcionario(Pessoa):
    def __init__(self, nome: str, endereco: str, codigo: str, salario:float) -> None:
        super().__init__(nome, endereco)
        self.codigo = codigo
        self.salario = salario

    def __repr__(self) -> str:
        return f'{type(self).__name__}(nome={self.nome},endereco={self.endereco},codigo={self.codigo},salario={self.salario})'
    
    def __str__(self) -> str:        
        return f'Nome:{self.nome}\nEndereço: {self.endereco}\nCódigo: {self.codigo}\nSalário:{self.salario}'

class Cliente(Pessoa):
    def __init__(self, nome: str, endereco: str, cpf:str, agencia:Agencia) -> None:
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.conta_bancaria = {'poupanca': [], 'corrente': []}
        self.agencia = agencia

    def adicionar_poupanca(self, conta:Poupanca):
        self.conta_bancaria['poupanca'].append(conta)
        return True

    def adicionar_corrente(self, conta:Corrente):
        self.conta_bancaria['corrente'].append(conta)
        return True
    
    @property
    def poupanca(self):
        if self.conta_bancaria['poupanca'] == []:
            return 'Nenhuma conta poupança'
        contas = ''
        for conta_poupanca in self.conta_bancaria['poupanca']:
            contas += f'{str(conta_poupanca)}\n'

        return contas
    
    @property
    def corrente(self):
        if self.conta_bancaria['corrente'] == []:
            return 'Nenhuma conta corrente'
        contas = ''
        for conta_corrente in self.conta_bancaria['corrente']:
            contas += f'{str(conta_corrente)}\n'

        return contas
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}(nome={self.nome},endereco={self.endereco},cpf={self.cpf},agencia={repr(self.agencia)},conta_bancaria,{self.conta_bancaria})'
    
    def __str__(self) -> str:        
        return f'Nome:{self.nome}\nEndereço: {self.endereco}\nCPF: {self.cpf}\nAgência:{self.agencia}\nPoupança:{self.poupanca}\nCorrente:{self.corrente}'

# Criando uma agência
agencia_central = Agencia(numero_agencia=101, cidade='São Paulo', endereco='Avenida Paulista, 1000')

# Criando um cliente e associando a agência
cliente_joao = Cliente(nome='João Silva', endereco='Rua das Flores, 123', cpf='123.456.789-00', agencia=agencia_central)
print("--------------------------- Dados do cliente João --------------------")
print(cliente_joao)
print("----------------------------------------------------------------------")
# Criando contas poupança e corrente
conta_poupanca_joao = Poupanca(numero_conta=202020, saldo=5000.0)
conta_corrente_joao = Corrente(numero_conta=101010, saldo=1000.0)

# Associando as contas ao cliente
cliente_joao.adicionar_poupanca(conta_poupanca_joao)
cliente_joao.adicionar_corrente(conta_corrente_joao)
print('---------------- Dados da conta bancária de João ---------------------')
print(cliente_joao.poupanca)
print(cliente_joao.corrente)
print('----------------------------------------------------------------------')
# Depositando dinheiro na conta corrente
print('----------------- Depósito na conta bancária de João -----------------')
conta_corrente_joao.depositar(500)
print(conta_corrente_joao)
print('----------------------------------------------------------------------')
# Tentando sacar mais do que o saldo disponível na conta poupança
saque_realizado = conta_poupanca_joao.sacar(6000)
print(f"Saque realizado: {saque_realizado}")
print(conta_poupanca_joao)
print('------------------ Transferência da conta bancária de João -----------')
# Definindo um limite na conta corrente
conta_corrente_joao.limite = 2000

# Transferindo da conta corrente para a conta poupança
transferencia_realizada = conta_corrente_joao.transferir(conta_destino=conta_poupanca_joao, valor=500)
print(f"Transferência realizada: {transferencia_realizada}")
print(conta_corrente_joao)
print(conta_poupanca_joao)
print('-----------------------------------------------------------------------')
print('------------------- Funcionário do banco ------------------------------')
# Criando um funcionário
funcionario_maria = Funcionario(nome='Maria Oliveira', endereco='Rua do Comércio, 45', codigo='F123', salario=3500.0)

print(funcionario_maria)
print('-----------------------------------------------------------------------')

# Criando a agência
agencia_central = Agencia(numero_agencia=101, cidade='São Paulo', endereco='Avenida Paulista, 1000')

# Criando os clientes
cliente_joao = Cliente(nome='João Silva', endereco='Rua das Flores, 123', cpf='123.456.789-00', agencia=agencia_central)
cliente_maria = Cliente(nome='Maria Oliveira', endereco='Rua do Comércio, 45', cpf='987.654.321-00', agencia=agencia_central)

# Criando contas para João e Maria
conta_poupanca_joao = Poupanca(numero_conta=202020, saldo=5000.0)
conta_corrente_joao = Corrente(numero_conta=101010, saldo=1000.0)
conta_poupanca_maria = Poupanca(numero_conta=303030, saldo=2000.0)
conta_corrente_maria = Corrente(numero_conta=404040, saldo=1500.0)

# Associando as contas aos clientes
cliente_joao.adicionar_poupanca(conta_poupanca_joao)
cliente_joao.adicionar_corrente(conta_corrente_joao)
cliente_maria.adicionar_poupanca(conta_poupanca_maria)
cliente_maria.adicionar_corrente(conta_corrente_maria)

print('----------------------- Operação de Bancária de saque e depósito -----------------')
# João realiza um saque e um depósito
print("Saldo João antes do saque:", conta_poupanca_joao.saldo)
conta_poupanca_joao.sacar(1000)
print("Saldo João após saque:", conta_poupanca_joao.saldo)
conta_corrente_joao.depositar(500)
print("Saldo João na conta corrente após depósito:", conta_corrente_joao.saldo)
print('----------------------------------------------------------------------------------\n')
print('----------- Transferência entre as contas bancárias de João e Maria --------------')
# Maria realiza uma transferência para a conta corrente de João
conta_corrente_maria.limite = 2000  # Definindo limite na conta corrente de Maria
transferencia_sucesso = conta_corrente_maria.transferir(conta_destino=conta_corrente_joao, valor=1000)
print("Transferência Maria -> João realizada com sucesso:", transferencia_sucesso)
print("Saldo João na conta corrente após transferência:", conta_corrente_joao.saldo)
print("Saldo Maria na conta corrente após transferência:", conta_corrente_maria.saldo)
print('-----------------------------------------------------------------------------------\n')
# Consultando os saldos das contas dos clientes
print("------------------------------- Saldos Finais ---------------------------------------")
print(f"João - Poupança: {conta_poupanca_joao.saldo}")
print(f"João - Corrente: {conta_corrente_joao.saldo}")
print(f"Maria - Poupança: {conta_poupanca_maria.saldo}")
print(f"Maria - Corrente: {conta_corrente_maria.saldo}")
print('-------------------------------------------------------------------------------------')

# Criando múltiplos clientes
print('----------------------------- Criando várias contas bancárias -----------------------')
clientes = []
for i in range(1, 6):
    cliente = Cliente(nome=f'Cliente {i}', endereco=f'Endereço {i}', cpf=f'000.000.000-{i:02d}', agencia=agencia_central)
    conta_poupanca = Poupanca(numero_conta=20000 + i, saldo=1000.0 * i)
    conta_corrente = Corrente(numero_conta=10000 + i, saldo=500.0 * i)
    cliente.adicionar_poupanca(conta_poupanca)
    cliente.adicionar_corrente(conta_corrente)
    clientes.append(cliente)
print('------------------------------------------------------------------------------------\n')
print('------------------------- Operações em várias contas bancárias -----------------------')
# Realizando depósitos e saques para todos os clientes
for cliente in clientes:
    cliente.conta_bancaria['poupanca'][0].depositar(500)
    cliente.conta_bancaria['corrente'][0].sacar(200)
    print(cliente)
    print("Saldo atualizado da Poupança:", cliente.conta_bancaria['poupanca'][0].saldo)
    print("Saldo atualizado da Corrente:", cliente.conta_bancaria['corrente'][0].saldo)
    print("-" * 40)
print('-----------------------------------------------------------------------------------\n')
print('-------------------- Transferência em várias contas bancárias -----------------------')
# Transferindo valores entre contas de diferentes clientes
clientes[0].conta_bancaria['corrente'][0].limite = 1000
clientes[1].conta_bancaria['corrente'][0].limite = 1500
transferencia_sucesso = clientes[0].conta_bancaria['corrente'][0].transferir(clientes[1].conta_bancaria['corrente'][0], 300)
print("Transferência Cliente 1 -> Cliente 2 realizada com sucesso:", transferencia_sucesso)
print(f"Saldo Cliente 1 - Corrente: {clientes[0].conta_bancaria['corrente'][0].saldo}")
print(f"Saldo Cliente 2 - Corrente: {clientes[1].conta_bancaria['corrente'][0].saldo}")
print('-------------------------------------------------------------------------------------')