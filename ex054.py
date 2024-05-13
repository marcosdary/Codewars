from abc import ABC, abstractmethod
class Conta(ABC):
    
    def __init__(self, saldo:float) -> None:
        self._saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
        
    def depositar(self, deposito:float) :
        
        if deposito > 0:
            self.saldo += deposito
            
        else:
            raise ValueError("Não há dinheiro negativo")
        
    @abstractmethod
    def sacar(self, saque): ...
    
class ContaCorrente(Conta):
    
    def sacar(self, saque) -> bool:
    
        if saque > 0 and saque <= self._saldo:
            self._saldo -= saque
            return True
        
        else:
            raise ValueError('Valor acima do disponível em sua conta ou valor para saque é negativo')

class ContaPoupanca(Conta):
    
    def sacar(self, saque) -> bool:
    
        if saque > 0 and saque <= self._saldo:
            
            self._saldo -= (saque * 1.02)
            return True
        
        else:
            raise ValueError('Valor acima do disponível em sua conta ou valor para saque é negativo')
        

        
    
conta_poupancao = ContaPoupanca(20_000)
print(conta_poupancao.saldo)
conta_poupancao.sacar(2_000)
print(conta_poupancao.saldo)

        
        
    
               
        