class ContaCorrente:
    def __init__(self, numero, titular) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0
        
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, valor: int):
        if valor < 0:
            raise ValueError("Número da conta incorreto")
        self.__numero = valor
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, valor: str):
        if valor.isalpha():
            raise ValueError("Nome do títular inválido")
        self.__titular = valor
        
    @property
    def saldo(self):
        return self.__saldo
    
    def deposito(self, dep:float):
        if dep > 0:
            self.__saldo += dep
            return True
        return False
    
    def saque(self, saq:float):
        if 0 < saq and saq <= self.__saldo:
            self.__saldo -= saq
            return True
        return False
        
    def transferencia(self, conta_destino, transf: float):
        if self.saque(transf):
            conta_destino(transf)
            return True
        return False