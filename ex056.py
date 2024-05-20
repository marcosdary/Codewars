class Conta:
    
    def __init__(self, titular, numero) -> None:
        self._titular = titular
        self._numero = numero
        self._saldo = 0
        
    
    def depositar(self, valor:float): 
        if valor < 0:
            raise ValueError("Não dinheiro negativo")
        self._saldo += valor
        return 'Depósito realizado com sucesso!!!'

    def sacar(self, valor:float):
        if valor <= self._saldo:
            self._saldo -= valor
            return 'Saque realizado com sucesso!!!'        
        else:
            raise ValueError("Saldo menor que saque pedido")  
              
    @property
    def consultar_saldo(self):
        return self._saldo
    
class ContaCorrente(Conta):
    
    def __init__(self, titular, numero, taxa_mensal) -> None:
        super().__init__(titular, numero)
        self.__taxa_mensal = taxa_mensal
    
        
class ContaPoupanca(Conta):
    def __init__(self, titular, numero, taxa_juros) -> None:
        super().__init__(titular, numero)
        self.__taxa_juros = taxa_juros
    
    def render_juros(self):
        taxa_juros = self._saldo * self.__taxa_juros/100
        self._saldo += taxa_juros
        
conta_corrente = ContaCorrente("João Silva", 12345, 0.1)
conta_poupanca = ContaPoupanca("Maria Oliveira", 54321, 1.0)

conta_corrente.depositar(1000.00)
print(conta_corrente.sacar(500.00))
print(conta_corrente.consultar_saldo)  # Resultado: 500.0

conta_poupanca.depositar(2000.00)
conta_poupanca.render_juros()
print(conta_poupanca.consultar_saldo) 